from django.shortcuts import render, redirect
from . import forms
from . import models
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

@method_decorator(login_required, name='dispatch')
class AddCarCreateView(CreateView):
    model = models.Car
    form_class = forms.CarForm
    template_name = 'add_car.html'
    success_url = reverse_lazy('add_car')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class DetailCarView(DetailView):
    model = models.Car
    pk_url_kwarg = 'id'
    template_name = 'car_details.html'
    
    def car(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        car = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = car
            new_comment.save()
        return self.get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        car = self.get_object()
        comment_form = forms.CommentForm(data=request.POST)
        
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = car
            new_comment.save()

            return redirect('detail_car', id=car.id)
        
        if car.quantity > 0:
            car.quantity -= 1
            car.save()   
            car.purchased_by.add(request.user) 

            messages.success(request, f'You have purchased {car.car_title}')
            return redirect('profile')
        else:
            messages.warning(request, 'This car is out of stock.')
            return redirect('homepage')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.get_object()
        comments = car.comments.all()
        comment_form = forms.CommentForm()

        context['comments'] = comments
        context['comment_form'] = comment_form
        return context
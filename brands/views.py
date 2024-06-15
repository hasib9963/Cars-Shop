from django.shortcuts import render, redirect
from . import forms


def add_brand(request):
    if request.method == 'POST':
        brand_form = forms.BrandForm(request.POST)
        if brand_form.is_valid():
            brand_form.save() 
            return redirect('add_brand') 
    
    else:
        brand_form = forms.BrandForm()
    return render(request, 'add_brand.html', {'brand_form' : brand_form})
from django import forms
from .models import Car, Comment

class CarForm(forms.ModelForm):
    class Meta: 
        model = Car
        # fields = '__all__'
        exclude = ['owner', 'purchased_by']
        
        
class CommentForm(forms.ModelForm):
    class Meta: 
        model = Comment
        fields = ['name', 'Comments']


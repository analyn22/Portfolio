from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django import forms

class Contact_form(ModelForm):
    class Meta:
        model = Contact
        fields = ['name','email','description']
        widgets = {
            'name':forms.TextInput(attrs={'class':'contact__input','placeholder':'Name'}),
            'email':forms.EmailInput(attrs={'class':'contact__input','placeholder':'Email'}),
            'description':forms.Textarea(attrs={'class':'contact__input','placeholder':'Message'}),
              
        }
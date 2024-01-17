from django import forms
from .models import *
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.core import validators

class LoginForm(forms.Form):
  username = forms.CharField(widget=forms.TextInput(attrs={
    'placeholder': 'Your username',
    'class': 'w-full py-4 px-6 rounded-xl',
  }))

  password = forms.CharField(widget=forms.PasswordInput(attrs={
    'placeholder': 'Your password',
    'class': 'w-full py-4 px-6 rounded-xl',
  }))


class RegisterForm(forms.Form):
  email_regex = RegexValidator(
        regex=r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+$',
        message="Enter the correct email input.",
    )

  username = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
    'placeholder': 'your username',
    'class': 'w-full py-4 px-6 rounded-xl',
  }))
  email = forms.EmailField(validators=[email_regex]
                           ,widget=forms.EmailInput(attrs={
    'placeholder': 'your username',
    'class': 'w-full py-4 px-6 rounded-xl',
  }))
  password = forms.CharField(widget=forms.PasswordInput(attrs={
    'placeholder': 'Your Password',
    'class': 'w-full py-4 px-6 rounded-xl',
  }))
  

INPUT_CLASS = 'w-full py-4 px-6 rounded-xl border'

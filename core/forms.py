from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth.models import User

class SingupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-fill py-4 px-6 rounded-xl'
    }))
    email = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Email',
        'class': 'w-fill py-4 px-6 rounded-xl'
    }))
    password1 = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your password1',
        'class': 'w-fill py-4 px-6 rounded-xl'
    }))
    password2 = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your password repeat',
        'class': 'w-fill py-4 px-6 rounded-xl'
    }))

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-fill py-4 px-6 rounded-xl'
    }))
    password = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-fill py-4 px-6 rounded-xl'
    }))


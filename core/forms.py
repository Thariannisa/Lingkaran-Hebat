from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'name', 'umur', 'avatar',  "password1", "password2"]
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Masukkan nama anda'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'type': 'email',
                    'placeholder': 'Masukkan email anda'
                }
            ),
            'umur': forms.TextInput(
                attrs={
                    'type': 'number',
                    'class': 'form-control',
                    'placeholder': 'Masukkan umur anda'
                }
            ),
            'avatar': forms.FileInput(
                attrs={
                    'class': 'custom-file-input',
                }
            ),
        }

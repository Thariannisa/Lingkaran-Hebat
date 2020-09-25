from django import forms
from .models import Riwayat


class RiwayatForm(forms.ModelForm):
    class Meta:
        model = Riwayat
        fields = ['title', 'description', 'time', 'image']
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control mb-2',
                    'placeholder': 'Masukkan title anda'
                }
            ),
            'description': forms.TextInput(
                attrs={
                    'class': 'form-control mb-2',
                    'placeholder': 'Masukkan description anda'
                }
            ),
            'time': forms.TextInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control mb-2',
                }
            ),
        }

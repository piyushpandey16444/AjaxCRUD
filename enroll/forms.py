from django import forms
from .models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["name", "email", "password"]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'form__name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'form__email'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'id': 'form__password'}),
        }
from django import forms
from .models import User


class UserForm(forms.ModelForm):
    """form for user in admin panel"""
    class Meta:
        model = User
        fields = ('id', 'email', 'password')
        widgets = {'id': forms.TextInput, 'email': forms.EmailInput, 'password': forms.TextInput}

from django import forms
from django.db.models.base import Model
from django.forms import fields
from django.forms.widgets import Input
from .models import Author
from django.forms import EmailField, CharField, IntegerField, DateInput, DateTimeInput


class AuthorForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Author
        fields = ('username', 'first_name', 'last_name', 'image', 'password')
        widgets = {
            'first_name': Input(attrs={'placeholder': 'Enter Name'}),
            'last_name': Input(attrs={'placeholder': 'Enter Surname'}),
        }

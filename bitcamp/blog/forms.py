from dataclasses import field
from pyexpat import model
from statistics import mode
from django import forms
from user.models import Author
from .models import Comment


class CommentForm(forms.Form):
    text = forms.CharField(max_length=255, label='Comment Name No')
    author = forms.CharField(max_length=155)


class CommetModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
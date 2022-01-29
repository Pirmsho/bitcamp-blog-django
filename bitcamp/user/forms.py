from django import forms
from django.db.models.base import Model
from django.forms import fields
from django.forms.widgets import Input
from .models import Author
from django.forms import EmailField, CharField, IntegerField, DateInput, DateTimeInput
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError


class AuthorForm(forms.ModelForm):
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
            help_text=password_validation.password_validators_help_text_html(),
            )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
                help_text=_("Enter the same password as before, for verification."), 
        )
    
    error_messages = {
        'password_mismatch': _('The two password fields don’t match.'),
        }

    class Meta:
        model = Author
        fields = ('username', 'first_name', 'last_name', 'image', 'password1', 'password2')
        widgets = {
            'first_name': Input(attrs={'placeholder': 'Enter NName'}),
            'last_name': Input(attrs={'placeholder': 'Enter Surname'}),
        }


    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def _post_clean(self):
        super()._post_clean()
        # Validate the password after self.instance is updated with form data
        # by super().
        password = self.cleaned_data.get('password2')
        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except ValidationError as error:
                self.add_error('password2', error)


    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

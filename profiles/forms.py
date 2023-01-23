from django import forms
from .models import User
from django.contrib.auth.forms import UserChangeForm, SetPasswordForm


class CustomUserChangeForm(UserChangeForm):
    password = forms.CharField(widget=forms.PasswordInput, required=False)
    class Meta:
        model = User
        fields = ('password',)

# class CustomPasswordChangeForm(SetPasswordForm):
    # new_password1 = forms.CharField(widget=forms.PasswordInput)
    # new_password2 = forms.CharField(widget=forms.PasswordInput)
    # class Meta:
    #     model  = User
    #     fields = ('password',)
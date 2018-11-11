from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.utils.translation import gettext, gettext_lazy as _
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label=_("Email"), max_length=254,widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(
                    widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                    label=_("Password"),
                    strip=False,
                    help_text=password_validation.password_validators_help_text_html(),
                )
    password2 = forms.CharField(
                    label=_("Password confirmation"),
                    widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                    strip=False,
                    help_text=_("Enter the same password as before, for verification."),
                )   
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'pizza_love')

class LoginForm(AuthenticationForm):
        username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
        password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

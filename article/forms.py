from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(forms.Form):

    username = forms.CharField(
        label='Your Username', widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    email = forms.EmailField(
        label='Your Email', widget=forms.EmailInput(
            attrs={'class': 'form-control'}
        )
    )


class RegistrationModelForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class RegistrationUserForm(UserCreationForm):
    username = forms.CharField(
        label='Your Username', widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    email = forms.EmailField(
        label='Your Email', widget=forms.EmailInput(
            attrs={'class': 'form-control'}
        )
    )

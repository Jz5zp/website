from django import forms
from django.contrib import auth
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', required=True, widget=forms.TextInput(
                                   attrs={'class': 'form-control', 'placeholder': 'Please enter username'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(
                                                    attrs={'class': 'form-control', 'placeholder': 'Please enter password'}))

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        user = auth.authenticate(username=username, password=password)
        if user is None:
            raise forms.ValidationError('Wrong Username or Password')
        else:
            self.cleaned_data['user'] = user
        return self.cleaned_data


class RegForm(forms.Form):
    username = forms.CharField(label='Username',
                               max_length=30,
                               min_length=3,
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control', 'placeholder': 'Please enter username'}))
    email = forms.EmailField(label='E-mail',
                             widget=forms.EmailInput(
                                 attrs={'class': 'form-control', 'placeholder': 'Please enter E-mail'}))
    password = forms.CharField(label='Code',
                               min_length=6,
                               widget=forms.PasswordInput(
                                   attrs={'class': 'form-control', 'placeholder': 'Please enter your code'}))
    password_again = forms.CharField(label='Code again',
                                     min_length=6,
                                     widget=forms.PasswordInput(
                                         attrs={'class': 'form-control', 'placeholder': 'Please enter your code again'}))

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Username Exists')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('E-mail Exists')
        return email

    def clean_password_again(self):
        password = self.cleaned_data['password']
        password_again = self.cleaned_data['password_again']
        if password != password_again:
            raise forms.ValidationError('Code is not matched')
        return password_again

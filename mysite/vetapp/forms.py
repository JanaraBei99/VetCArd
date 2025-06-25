from django import forms
from django.contrib.auth.hashers import make_password
from mysite.users.models import User, UserProfile


class CustomLoginForm(forms.Form):
    login = forms.CharField(label='Логин')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')
    password_confirm = forms.CharField(widget=forms.PasswordInput, label='Повторите пароль')
    first_name = forms.CharField(max_length=100, label='Имя')
    last_name = forms.CharField(max_length=100, label='Фамилия')
    surname = forms.CharField(max_length=100, label='Отчество')
    email = forms.EmailField(label='Email')

    class Meta:
        model = User
        fields = ['login', 'role']


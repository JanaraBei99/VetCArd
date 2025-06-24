from django import forms
from .models import Users, Role


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.CharField(widget=forms.EmailInput)
    role = forms.ModelChoiceField(
        queryset=Role.objects.all(),
        empty_label="Выберите роль",
        label="Роль",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Users
        fields = ['login', 'email', 'password', 'role']

class CustomLoginForm(forms.Form):
    login = forms.CharField(label='Логин')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')


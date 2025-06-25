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

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        if password and password_confirm and password != password_confirm:
            self.add_error('password_confirm', "Пароли не совпадают")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data['password'])  # Хешируем пароль
        if commit:
            user.save()
            UserProfile.objects.create(
                user=user,
                first_name=self.cleaned_data['first_name'],
                last_name=self.cleaned_data['last_name'],
                surname=self.cleaned_data['surname'],
                email=self.cleaned_data['email']
            )
        return user

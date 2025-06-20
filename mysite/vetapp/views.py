from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from .models import Users  # твоя модель
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login
from django.contrib.auth.hashers import check_password
from .forms import CustomLoginForm
from django.contrib.auth import logout

def index(request):
    return render(request, 'vetapp/index.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'vetapp/register.html', {'form': form})

def user_login(request):
    error = ''
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            login_input = form.cleaned_data['login']
            password_input = form.cleaned_data['password']

            try:
                user = Users.objects.get(login=login_input)
                if check_password(password_input, user.password):
                    request.session['user_id'] = user.id
                    return redirect('index')  # redirect на главную страницу
                else:
                    error = 'Неверный пароль'
            except Users.DoesNotExist:
                error = 'Пользователь не найден'
    else:
        form = CustomLoginForm()
    return render(request, 'vetapp/login.html', {'form': form, 'error': error})

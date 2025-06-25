from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password, make_password
from .forms import UserRegistrationForm, CustomLoginForm
from .models import Users, UserProfile

def index(request):
    return render(request, 'vetapp/index.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  # в форме хешируем пароль и создаём профиль
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
                    request.session['user_id'] = user.user_id
                    return redirect('index')
                else:
                    error = 'Неверный пароль'
            except Users.DoesNotExist:
                error = 'Пользователь не найден'
    else:
        form = CustomLoginForm()
    return render(request, 'vetapp/login.html', {'form': form, 'error': error})

def user_logout(request):
    request.session.flush()
    return redirect('login')

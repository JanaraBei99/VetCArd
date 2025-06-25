from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, CustomLoginForm
from .models import Users
from django.contrib.auth.hashers import check_password, make_password

def index(request):
    return render(request, 'vetapp/index.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # форма сама создает пользователя и профиль, хеширует пароль
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
                    request.session['user_id'] = user.user_id  # user.user_id, если в модели primary key user_id
                    return redirect('index')
                else:
                    error = 'Неверный пароль'
            except Users.DoesNotExist:
                error = 'Пользователь не найден'
    else:
        form = CustomLoginForm()
    return render(request, 'vetapp/login.html', {'form': form, 'error': error})

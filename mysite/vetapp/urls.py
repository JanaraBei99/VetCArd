from django.shortcuts import render
from django.urls import path
from . import views
from django.urls import path



urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('success/', lambda request: render(request, 'success.html'), name='success'),
    path('login/', views.user_login, name='login'),
]

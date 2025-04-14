"""Модуль views для регистрации и входа пользователей."""
import re
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

#Проверяем допустимость логина
def is_valid(login) -> bool:
    """Проверяет допустимость логина по регулярному выражению

        Аргументы:
            login_str (str): Проверяемый логин

        Вывод функции:
            bool: True если логин соответствует шаблону
        """

    pattern = r'^[a-zA-Z0-9_]+$'
    return re.match(pattern, login) is not None

def signup(request):
    """Обрабатывает регистрацию новых пользователей"""
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        email = request.POST.get('email', '')
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # Проверяем пароли
        if password1 != password2:
            messages.error(request, 'Пароли не совпадают')
            return redirect('signup')

        # Проверяем допустимость логина
        if not is_valid(username) :
            messages.error(request,
                    'Логин может содержать только латинские буквы, цифры и нижнее подчеркивание')
            return redirect('signup')

        # Проверяем уникальность логина
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Логин уже занят')
            return redirect('signup')

        # Создаем пользователя
        user = User.objects.create_user(username=username, password=password1,
                                        first_name=first_name, email=email)
        user.save()

        #Перенаправление после успешной регистрации на страницу входа
        messages.success(request, 'Регистрация пройдена успешно! Войдите с введенными данными.')
        return redirect('login')

    return render(request, 'signup.html')

def user_login(request):
    """Обрабатывает авторизацию пользователей."""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Неверный пароль')
        except:
            messages.error(request, 'Пользователь не найден')
    return render(request, 'login.html')

@login_required
def user_logout(request):
    """Обрабатывает выход пользователя из системы."""
    logout(request)
    return redirect('login.html')

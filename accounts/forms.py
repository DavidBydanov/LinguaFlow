"""Модуль регистрации пользователей в приложении accounts"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    """Форма регистрации пользователя

        Наследует стандартную форму UserCreationForm и добавляет:
        - Поле для имени (first_name)
        - Опциональное поле email
        """

    first_name = forms.CharField(
        max_length=30,
        required=True,
        label="Имя",
        widget=forms.TextInput(attrs={'class': 'form-control'}))

    email = forms.EmailField(
        required=False,
        label="E-mail (необязательно)",
        widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        """Мета-класс для настройки базовой формы"""
        model = User
        fields = ('username', 'first_name', 'email', 'password1', 'password2')
        labels = {
            'username': 'Логин',
            'first_name': 'Имя',
            'email': 'E-mail (необязательно)',
            'password1': 'Пароль',
            'password2': 'Повторите пароль',
        }
"""Модуль форм для работы с карточками и грамматическими заметками"""
from django import forms
from .models import Card, GrammarNote

class CardForm(forms.ModelForm):
    """Класс для создания и редактирования карточек со словами"""
    class Meta:
        """Мета-класс для настройки формы карточки"""
        model = Card
        fields = ['word', 'transcription', 'translation']
        widgets = {
            'word': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'transcription': forms.TextInput(attrs={'class': 'form-control'}),
            'translation': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            }

class GrammarNoteForm(forms.ModelForm):
    """Класс для создания и редактирования заметок по грамматике"""
    class Meta:
        """Мета-класс для настройки формы заметки"""
        model = GrammarNote
        fields = ['title', 'content', 'examples']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Введите название заметки',
                                            'required': True}),
            'content': forms.Textarea(attrs={'class': 'form-control',
                                             'rows': 4,
                                             'placeholder': 'Опишите грамматическое правило',
                                             'required': True}),
            'examples': forms.Textarea(attrs={'class': 'form-control',
                                              'rows': 3,
                                              'placeholder': 'Приведите примеры использования'})
        }
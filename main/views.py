"""Модуль представлений для работы с карточками и заметками."""
import json
from django.shortcuts import render, redirect
from .models import Card, GrammarNote
from .forms import CardForm, GrammarNoteForm
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    """Главная страница с отображением всех материалов сайта"""
    cards = Card.objects.order_by('word')
    grammar_notes = GrammarNote.objects.all()
    return render(request, 'home.html', {'cards': cards, 'grammar_notes': grammar_notes})

@login_required
def add_card(request):
    """Обработка добавления новых карточек"""
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

@login_required
def add_grammar(request):
    """Обработка добавления новых заметок"""
    if request.method == 'POST':
        form = GrammarNoteForm(request.POST)
        if form.is_valid():
            new_note = form.save(commit=False)
            new_note.save()
            return redirect('home')

@login_required
def start_training(request):
    """Переход на странице тренировки"""
    cards = list(Card.objects.all().order_by('?').values('word', 'transcription', 'translation'))
    return render(request, 'training.html', {'cards': json.dumps(cards, default=str)})

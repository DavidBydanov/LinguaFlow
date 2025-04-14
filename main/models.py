"""Модели приложения для работы с карточками и заметками"""
from django.db import models

class Card(models.Model):
    """Модель карточки со словами"""
    word = models.CharField(max_length=100, verbose_name="Слово")
    transcription = models.CharField(max_length=100, verbose_name="Транскрипция", default="", blank = True)
    translation = models.CharField(max_length=100, verbose_name="Перевод")


    def __str__(self) -> str:
        """Строковое представление карточки"""
        return self.word

    def to_dict(self) -> dict:
        """Преобразование в словарь"""
        return {'word': self.word,
                'transcription': self.transcription,
                'translation': self.translation}

class GrammarNote(models.Model):
    """Модель заметки с грамматикой"""
    title = models.CharField(max_length=200, verbose_name="Название")
    content = models.TextField(verbose_name="Содержание")
    examples = models.TextField(blank=True, verbose_name="Примеры")

    def __str__(self):
        """Строковое представление заметки"""
        return self.title
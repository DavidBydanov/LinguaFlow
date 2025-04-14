"""Вспомогательный скрипт для загрузки информация из xlsx-файла (для карточек) в БД проекта"""
import pandas as pd
from django.core.management.base import BaseCommand
from main.models import Card


class Command(BaseCommand):
    """Команда для загрузки карточек слов из Excel-файла"""
    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str)

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']

        try:
            df = pd.read_excel(file_path)
            words = []
            for index, row in df.iterrows():
                words.append(Card(
                    word=row['Слово'],
                    transcription=row['Транскрипция'],
                    translation=row['Перевод']))

            Card.objects.bulk_create(words)

            self.stdout.write(self.style.SUCCESS(
                f'Успешно импортировано {len(words)} записей'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(
                f'Ошибка импорта: {str(e)}'))

"""Вспомогательный скрипт для загрузки информация из xlsx-файла (заметки) в БД проекта"""
import pandas as pd
from django.core.management.base import BaseCommand
from main.models import GrammarNote


class Command(BaseCommand):
    """Команда для загрузки заметок из Excel-файла"""
    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str)

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']

        try:
            df = pd.read_excel(file_path)
            notes = []
            for index, row in df.iterrows():
                notes.append(GrammarNote(
                    title=row['Название'],
                    content=row['Содержание'],
                    examples=row['Примеры']))

            GrammarNote.objects.bulk_create(notes)

            self.stdout.write(self.style.SUCCESS(
                f'Успешно импортировано {len(notes)} записей'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(
                f'Ошибка импорта: {str(e)}'))

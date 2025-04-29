""" Command to import actors from a CSV file """
import csv
from datetime import datetime, date
from django.core.management.base import BaseCommand
from actors.models import Actor


class Command(BaseCommand):
    """ import actors from a CSV file """
    def add_arguments(self, parser):
        """Arguments for the command"""
        parser.add_argument(
            'file_name',
            type=str,
            help='The CSV file to import actors from'
        )

    def handle(self, *args, **options):
        """ method to handle the command """
        file_name = options['file_name']

        with open(file_name, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['name']
                birth_date = datetime.strptime(row['birth_date'], '%Y-%m-%d').date()
                nationality = row['nationality']

                self.stdout.write(self.style.NOTICE(f'{name} - imported successfully'))

                Actor.objects.create(
                    name=name,
                    birth_date=birth_date,
                    nationality=nationality
                )

        self.stdout.write(self.style.SUCCESS('Actors imported successfully'))

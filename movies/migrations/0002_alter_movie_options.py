# Generated by Django 5.1.7 on 2025-03-27 20:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movie',
            options={'ordering': ['title'], 'verbose_name': 'Movie', 'verbose_name_plural': 'Movies'},
        ),
    ]

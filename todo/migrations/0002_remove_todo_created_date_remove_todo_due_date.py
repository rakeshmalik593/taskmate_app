# Generated by Django 4.2 on 2023-04-15 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='due_date',
        ),
    ]

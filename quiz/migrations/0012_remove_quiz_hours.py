# Generated by Django 3.0.2 on 2020-06-17 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0011_attempt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='hours',
        ),
    ]

# Generated by Django 3.0.2 on 2020-06-12 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_quiz_instructions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='questions',
            field=models.IntegerField(),
        ),
    ]

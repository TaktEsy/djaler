# Generated by Django 2.1.1 on 2019-01-20 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appquestions', '0005_remove_questions_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='text',
            field=models.TextField(verbose_name='Текст ответа'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='text',
            field=models.TextField(verbose_name='Текст вопроса'),
        ),
    ]

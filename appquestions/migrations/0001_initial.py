# Generated by Django 2.1.1 on 2018-10-29 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(auto_now=True, verbose_name='Дата/время')),
                ('text', models.TextField(max_length=1500, verbose_name='Текст ответа')),
            ],
            options={
                'verbose_name': 'Ответ',
                'db_table': 'appquest_answers',
                'ordering': ['-date_time'],
                'verbose_name_plural': 'Ответы',
            },
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Категория',
                'db_table': 'appquest_categories',
                'ordering': ['name'],
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('text', models.TextField(max_length=2500, verbose_name='Текст вопроса')),
                ('published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('slug', models.SlugField(default='url-of-page', editable=False, help_text='Например, .../статьи/(номер статьи)', verbose_name='URL страницы')),
                ('date_time', models.DateTimeField(auto_now=True, verbose_name='Дата/время')),
            ],
            options={
                'verbose_name': 'вопрос',
                'db_table': 'appquest_questions',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.AddField(
            model_name='answers',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='appquestions.Questions', verbose_name='К какому вопросу'),
        ),
    ]

# Generated by Django 2.1.1 on 2018-11-04 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appquestions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='slug',
            field=models.SlugField(editable=False, verbose_name='URL страницы'),
        ),
    ]
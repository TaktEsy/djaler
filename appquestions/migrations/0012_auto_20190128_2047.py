# Generated by Django 2.1.1 on 2019-01-28 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appquestions', '0011_auto_20190120_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='URL страницы'),
        ),
    ]

# Generated by Django 2.1.1 on 2019-02-03 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appquestions', '0012_auto_20190128_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='slug',
            field=models.SlugField(editable=False, unique=True, verbose_name='URL страницы'),
        ),
    ]
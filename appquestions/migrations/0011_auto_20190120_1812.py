# Generated by Django 2.1.1 on 2019-01-20 18:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appquestions', '0010_auto_20190120_1812'),
    ]

    operations = [
        migrations.AddField(
            model_name='answers',
            name='author',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='questions',
            name='author',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
            preserve_default=False,
        ),
    ]

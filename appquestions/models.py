# -*- coding: utf-8 -*-
from django.contrib.auth.models import User

from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from autoslug import AutoSlugField
from typing import Any


class BaseAbstractAppQuest(models.Model):
	class Meta:
		abstract = True


class ExtAbstractAppQuest(BaseAbstractAppQuest):
	class Meta:
		abstract = True

	author = models.ForeignKey(User,verbose_name="Автор",on_delete=models.CASCADE)	
	text = models.TextField(verbose_name="Текст", max_length=1500)


# Categories of questions 
class Categories(models.Model):
	name = models.CharField(max_length=100, verbose_name="Название")

	class Meta(object):
		db_table = 'appquest_categories'
		ordering = ["name"]	
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'

	def __str__(self):
		return self.name


# Questions model
class Questions(ExtAbstractAppQuest):
	title = models.CharField(verbose_name="Заголовок", max_length=100)
	published = models.BooleanField(default=True, verbose_name="Опубликовано")
	# category = models.ForeignKey('questions.Categories', verbose_name="Категория", blank=False, default="Определите подходящую тему вопроса")
	slug = AutoSlugField(populate_from='title', verbose_name='URL страницы', editable=False, blank=False, unique=True)
	date_time = models.DateTimeField(auto_now=True, verbose_name="Дата/время")

	
	class Meta(object):
		db_table = 'appquest_questions'
		ordering = ["-date_time"]	
		verbose_name = 'Вопрос'
		verbose_name_plural = 'Вопросы'
	
	def __str__(self):
		return self.title


class Answers(ExtAbstractAppQuest):
	date_time = models.DateTimeField(auto_now=True, verbose_name="Дата/время")
	question = models.ForeignKey(Questions, verbose_name="К какому вопросу", on_delete=models.DO_NOTHING)

	class Meta(object):
		db_table = 'appquest_answers'
		ordering = ["-date_time"]
		verbose_name = 'Ответ'
		verbose_name_plural = 'Ответы'
		
	def __str__(self):
		return self.text

# @receiver(pre_save, sender=Questions)
# def pre_save_slug(sender, **kwargs):
# 	slug = slugify(kwargs['isnstance'].title)
# 	kwargs['isnstance'].slug = slug
# 	print("Hello, world!")
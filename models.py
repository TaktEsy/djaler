from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from extuser.models import ExtUser
from django.utils.text import slugify
from service_module import transliteration as translit
from ckeditor_uploader.fields import RichTextUploadingField


class AbstractAQModel(models.Model):
	date_time = models.DateTimeField(auto_now=True, verbose_name="Дата/время")
	hided = models.BooleanField(default=False, verbose_name="Скрыто")
	extuser = models.ForeignKey('extuser.ExtUser', verbose_name="Автор")
	likes = models.IntegerField('Кол-во лайков', default=0)
	dislikes = models.IntegerField('Кол-во дизлайков', default=0)

	class Meta:
		abstract = True

# Questions 
class Questions(AbstractAQModel):
	title = models.CharField(max_length=200, verbose_name="Заголовок")
	text = models.TextField(max_length=2500, verbose_name="Текст вопроса")
	published = models.BooleanField(default=True, verbose_name="Опубликовано")
	category = models.ForeignKey('questions.Categories', verbose_name="Категория", blank=False, default="Определите подходящую тему вопроса")
	slug = models.SlugField(default='url-of-page', verbose_name='URL страницы', help_text='Например, .../статьи/(номер статьи)', editable=False)
	
	def save(self, *args, **kwargs):
		self.slug = slugify(translit(self.title), allow_unicode=True)
		super(Questions, self).save(*args, **kwargs)

	class Meta(object):
		db_table = 'questions'
		ordering = ["-date_time"]	
		verbose_name = 'Вопрос'
		verbose_name_plural = 'Вопросы'
	
	def __str__(self):
		return '%s' % (self.title)

# Answers for questions 
class Answers(AbstractAQModel):
	text = models.TextField(verbose_name="Текст ответа", max_length=1500)
	question = models.ForeignKey(Questions, verbose_name="К какому вопросу")

	class Meta(object):
		db_table = 'questions_answer'
		ordering = ["-date_time"]
		verbose_name = 'Ответ'
		verbose_name_plural = 'Ответы'
	
	def get_absolute_url(self):
		return reverse()
		
	def __str__(self):
		return self.text

# Categories of questions 
class Categories(models.Model):
	name = models.CharField(max_length=100, verbose_name="Название")

	class Meta(object):
		db_table = 'questions_categories'
		ordering = ["name"]	
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'

	def __str__(self):
		return self.name


# Tags of questions 
class Tags(models.Model):
	tag = models.CharField(max_length=100, verbose_name="Тег")

	class Meta(object):
		db_table = 'questions_tags'
		ordering = ["tag"]	
		verbose_name = 'Тег'
		verbose_name_plural = 'Теги'

	def __str__(self):
		return self.tag
		
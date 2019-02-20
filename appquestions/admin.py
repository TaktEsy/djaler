from django.contrib import admin
from .models import *


class GeneralAdmin(admin.ModelAdmin):
	save_on_top = True
	ordering = ['-date_time']

class AnswersAdmin(GeneralAdmin):
	list_display_links = ('id', 'text',)
	list_display = ('id', 'text', 'date_time')

class CategoriesAdmin(GeneralAdmin):
	list_display = ('id', 'name',)
	list_display_links = ('id', 'name',)
	ordering = ['name']

class QuestionsAdmin(GeneralAdmin):
	# Отвечает за вывод в админке модуля с вопросами
	list_display = ('id', 'title', 'date_time', 'slug', 'published')
	list_display_links = ('id', 'title')

	list_filter = ('published', 'date_time')
	fields = ('author', 'title', 'text', 'published')

admin.site.register(Answers, AnswersAdmin)	
admin.site.register(Categories, CategoriesAdmin)	
admin.site.register(Questions, QuestionsAdmin)
from backends.ajaxmixin.edit import *
from backends.base import BaseProtection
from backends.abc.basic_abc import basicViewAbstract

from django.contrib.auth.decorators import login_required
from django.http import *
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.views.generic.detail import SingleObjectMixin
from django.utils.decorators import method_decorator



from random import *

from extuser.forms import LoginForm
from extuser.models import ExtUser
from .forms import *
from .models import *



class IndexPage(ListView, basicViewAbstract):
	context_object_name = 'general_array'
	template_name = 'questions/index_page.html'

	def get_queryset(self):
		
		
		#Обязательно добавить выборку записи за СЕГОДНЯ
		self.questions = Questions.objects.select_related("extuser__username").values("id", "title", "text", "date_time", "slug", "extuser__username", "category__name").filter(hided=False, published=True).order_by('?')[:3]
		
		# Math the num of answers to question with definite `id` 
		for question in self.questions:
			question['num_answers'] = Answers.objects.filter(question_id=question['id'], hided=False).count()

		# Pruning of fields called `title` and `text`
		for question in self.questions:	
			if (len(question["text"])>250):
				question["text"] = question["text"][:247]+"..."
			
			if (len(question["title"])>45):
					question["title"] = question["title"][:42]+"..."	
		
		return self.questions

	def get_context_data(self, *args, **kwargs):
		context = super(IndexPage, self).get_context_data(**kwargs)
		context['bestusers'] = ExtUser.objects.values("avatar", "username", "userscore__today_score", "userscore__level__level_name").order_by('-userscore__today_score')[:6]
		context["quick_auth_form"] = LoginForm
		return context

# Categories page
class CategoriesPage(ListView):
	template_name = 'questions/categories_page.html'		

	# def get(self, request, *args, **kwargs):
	# 	self.object = self.get_object(queryset=Categories.objects.all())
	# 	#super(QuestionPage, self).delete_attr(self.object.extuser, "password")
	# 	return super(CategoriesPage, self).get(request, *args, **kwargs)

	def get_queryset(self):
		
		return self.object


# Question page
class QuestionPage(BaseProtection, ListView, SingleObjectMixin):
	form_class = AnswerForm
	template_name = 'questions/question_page.html'
	slug_url_kwarg = 'question_slug'
		
	def get(self, request, *args, **kwargs):
		self.object = self.get_object(queryset=Questions.objects.select_related("extuser").all())
		#super(QuestionPage, self).delete_attr(self.object.extuser, "password")
		return super(QuestionPage, self).get(request, *args, **kwargs)
		
	def get_context_data(self, *args, **kwargs):
		context = super(QuestionPage, self).get_context_data(**kwargs)
		#super(QuestionPage, self).delete_attr(self.object.extuser, "password")
		context['question'] = self.object
		context['answers'] = Answers.objects.filter(question_id=self.object).values("date_time", "text", "extuser__avatar", 'extuser__username', "extuser__userscore__level__level_name")
		context['category_name'] = Categories.objects.filter(id=self.object.id).values('name',)
		context["quick_auth_form"] = LoginForm

		if self.request.user.is_authenticated(): 
			context['form_answ'] = AnswerForm(initial={'extuser': self.request.user.id, 'question': self.object.id})

		return context

	def get_queryset(self):
		return self.object


@method_decorator(login_required, name='dispatch')
class MakeAnswer(AjaxCreateView):
	form_class = AnswerForm
	model = Answers
	success_url = "./"

	def form_valid(self, form):
		exits_slug = Questions.objects.get(slug=form.instance.slug)
		if exits_slug:
			form.instance.slug = form.instance.slug+"-"+form.instance.id
		form.instance.extuser = self.request.user
		self.success_url = "/questions/"+instance.slug
		return super(QuestionMakeAnswer, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class MakeQuestionPage(CreateView):
	model = Questions
	form_class = MakeQuestionForm
	template_name = 'questions/make_question_form.html'
	success_url = "/"
	
	def form_valid(self, form):
		form.instance.extuser = self.request.user
		return super(MakeQuestionPage, self).form_valid(form)

	def get_context_data(self, *args, **kwargs):
		context = super(MakeQuestionPage, self).get_context_data(**kwargs)
		context["make_form"] = self.form_class
		return context
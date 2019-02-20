from .models import *
from .forms import *

from django.views.generic import ListView, DetailView

class IndexPage(ListView):
	context_object_name = 'general_array'
	template_name = 'index_page.html'
	model = Questions

	
	def get_queryset(self):
		self.questions = Questions.objects.values("id", "title", "text", "slug").filter(published=True).order_by('?')[:3]
		
		# !!!!!IN FUTURE TO MODEL!!!!! Pruning of fields called `title` and `text` 
		for question in self.questions:	
			if (len(question["text"])>250):
				question["text"] = question["text"][:247]+"..."
			
			if (len(question["title"])>45):
					question["title"] = question["title"][:42]+"..."	
		
		return self.questions
	# def get_context_data(self, *args, **kwargs):
		# context = super(IndexPage,self).get_context_data(**kwargs)
		# context['bestusers'] = User.objects.values("photo_medium", "username")

class QuestionPage(DetailView):
	form_class = AnswerForm
	template_name = 'question_page.html'
	slug_url_kwarg = 'slug'
	model = Questions



	def get_context_data(self, *args, **kwargs):
		context = super(QuestionPage, self).get_context_data(**kwargs)
		context['question'] = self.object
		context['answers'] = Answers.objects.filter(question_id=self.object).values("date_time", "text")
		context['form_answer'] = AnswerForm 
		
		

		return context
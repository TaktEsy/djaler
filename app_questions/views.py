from django.shortcuts import render
from django.views.generic import ListView


class IndexPage(ListView):
	context_object_name = 'general_array'
	template_name = 'questions/index_page.html'

	def get_queryset(self):
		'''[summary]
		
		[description]
		
		Returns:
			[type] -- [description]
		'''
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
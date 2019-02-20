from django.forms import HiddenInput, ModelForm, Textarea, TextInput, Select
from django import forms
from .models import Answers, Questions

class AnswerForm(ModelForm):
	class Meta:
		model = Answers
		fields = ["text"]
		widgets = {
			'text': Textarea(),
		}
		labels = {
			'text': (''),
		}

# class MakeQuestionForm(ModelForm):
# 	class Meta:
# 		model = Questions
# 		fields = ["title", "category", "text"]
# 		widgets = {
# 			'title': TextInput(attrs={'placeholder': 'Введите заголовок вопроса'}),
# 			'text': Textarea(attrs={'placeholder': 'Постарайтесь как можно информативнее передать суть вопроса'}),
# 			'category': Select(attrs={'placeholder': 'Укажите категорию вопроса'}),
# 		}
# 		labels = {
# 			'title': (''),
# 			'text': (''),
# 			'category': (''),
# 		}

# 	def clean(self):
# 		cleaned_data = super(MakeQuestionForm, self).clean()
# 		title = cleaned_data['title']
		

# 		if title == "categories" or title == "make_question":
# 			raise forms.ValidationError("Недопустимый заголовок вопроса!")
			
# 		return cleaned_data	
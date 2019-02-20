from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView


class ProfilePage(DetailView):
	template_name = 'profile_page.html'
	slug_url_kwarg = 'login'
	slug_field = 'username'
	model = User

	def get(self, request, *args, **kwargs):
		self.object = self.get_object(queryset=User.objects.filter(username=self.kwargs['login']))
		return super(ProfilePage, self).get(request, *args, **kwargs)

	# def get_queryset(self):
	# 	user = User.objects.get(username= )
	# 	context['user'] = self.object
			

	# 	return context
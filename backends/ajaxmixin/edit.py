from django.core.exceptions import ImproperlyConfigured
from django.http import JsonResponse
from django.views.generic.edit import FormView, ProcessFormView
from django.views.generic.detail import (SingleObjectMixin, SingleObjectTemplateResponseMixin,)

class AjaxFormMixin(FormView):
	template_name = "questions/index_page.html"

	def form_valid(self, form, response_ajax={'status':200}):
		if self.request.is_ajax():
			return JsonResponse(response_ajax)
		else:
			return super(AjaxFormMixin, self).form_valid(form)

	def form_invalid(self, form, response_ajax={'status':500}):
		serialized = dict([(k, [e for e in v]) for k, v in form.errors.items()])
		
		if self.request.is_ajax():
			return JsonResponse(serialized, safe=False)
		else:
			return super(AjaxFormMixin, self).form_invalid(form)


class AjaxModelFormMixin(AjaxFormMixin, SingleObjectMixin):
	"""
	A mixin that provides a way to show and handle a modelform in a request.
	"""
	fields = None

	def form_valid(self, form):
		"""
		If the form is valid, save the associated model.
		"""
		if self.request.is_ajax():
			self.object = form.save()
			return super(AjaxModelFormMixin, self).form_valid(form)
		else:
			return super(AjaxFormMixin, self).form_valid(form)	


class AjaxFormView(AjaxFormMixin, ProcessFormView):
	"""
	This class combines in itself `AjaxFormMixin` and `AjaxProcessFormView`
	
	Extends:
		AjaxFormMixin
		ProcessFormView
	"""


class AjaxBaseCreateView(AjaxModelFormMixin, ProcessFormView):
	"""
	Base view for creating an new object instance.
	Using this base class requires subclassing to provide a response mixin.
	"""
	def get(self, request, *args, **kwargs):
		self.object = None
		return super(AjaxModelFormMixin, self).get(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		self.object = None
		return super(AjaxModelFormMixin, self).post(request, *args, **kwargs)


class AjaxCreateView(SingleObjectTemplateResponseMixin, AjaxBaseCreateView):
	"""
	View for creating a new object instance,
	with a response rendered by template.
	"""
	template_name_suffix = '_form'


class AjaxBaseUpdateView(AjaxModelFormMixin, ProcessFormView):
	"""
	Base view for updating an existing object.
	Using this base class requires subclassing to provide a response mixin.
	"""
	def get(self, request, *args, **kwargs):
		self.object = self.get_object()
		return super(AjaxBaseUpdateView, self).get(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		self.object = self.get_object()
		return super(AjaxBaseUpdateView, self).post(request, *args, **kwargs)


class AjaxUpdateView(SingleObjectTemplateResponseMixin, AjaxBaseUpdateView):
	"""
	View for updating an object,
	with a response rendered by template.
	"""
	template_name_suffix = '_form'
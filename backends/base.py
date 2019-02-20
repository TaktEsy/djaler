# class OverridedBaseExeption(BaseException):
# 	"""docstring for OverridedBaseExeptions"""
from django.contrib.auth.mixins import LoginRequiredMixin

class BaseProtection():
	"""The base clase for safe work with DB, templates etc."""
	disallowed_fields = ('email', 'password')
	
	def delete_attr(self, obj, *args):
		"""
		Function accept `obj`, in which will be deleted all 
		fields that names there are in `args`

		For every new object, subobject - new call [bug :( ]
		"""
		if not args:
			args = self.disallowed_fields
		for field in args:
			if hasattr(obj, field):
				setattr(obj, field, None)
		return obj
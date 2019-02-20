from abc import ABCMeta, abstractmethod, abstractproperty

class basicViewAbstract(object):
	"""basicAbstract is responsible for observation of all rules in views (forms, modules, etc.)"""
	__metaclass__=ABCMeta
	
	@abstractproperty
	def size(self):
		pass	
	
	@abstractmethod
	def size2(self):
		pass	
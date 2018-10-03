"""djaler URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import *

urlpatterns = [
	path(r'^(?P<question_slug>[A-Za-z0-9-]+)/$', IndexPage.as_view(), name='question'),
]
"""
	path(r'^(?P<question_slug>[A-Za-z0-9-]+)/$', QuestionPage.as_view(), name='question'),
	path(r'^make_question/$', MakeQuestionPage.as_view(), name='make_question'),
	path(r'^(?P<question_slug>[A-Za-z0-9-]+)/make_answer/$', MakeAnswer.as_view(), name='make_answer'),
"""
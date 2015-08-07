"""coachsurveys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url

from . import views

urlpatterns = [
    #SURVEY
    url(r'^$', views.survey_list, name='survey_list'),
    url(r'^new$', views.survey_create, name='survey_new'),
  	url(r'^edit/(?P<pk>\d+)$', views.survey_update, name='survey_edit'),
  	url(r'^(?P<pk>\d+)/$', views.survey_view, name='survey_view'),
  	url(r'^delete/(?P<pk>\d+)$', views.survey_delete, name='survey_delete'),

  	#QUESTIONS
  	url(r'^(?P<survey_id>\d+)/questions/new/$', views.question_create, name='question_new'),
  	url(r'^(?P<survey_id>\d+)/questions/edit/(?P<question_id>\d+)$', views.question_update, name='question_edit'),
  	url(r'^(?P<survey_id>\d+)/questions/view/(?P<question_id>\d+)$', views.question_view, name='question_view'),
  	url(r'^(?P<survey_id>\d+)/questions/delete/(?P<question_id>\d+)$', views.question_delete, name='question_delete'),

    #CHOICES
    # url(r'^(?P<question_id>\d+)/choice/new/$', views.choice_create, name='choice_new'),


]

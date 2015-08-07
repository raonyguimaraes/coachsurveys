from django.db import models
# from django.contrib.auth.models import User
from authtools.models import User

# Create your models here.
class Survey(models.Model):
	title = models.CharField(max_length=50)
	description = models.TextField()
	created_date = models.DateField(auto_now_add=True, editable=False)
	modified_date = models.DateField(auto_now=True)
	user = models.ForeignKey(User)


class Question(models.Model):
	survey = models.ForeignKey(Survey)
	question_type = models.CharField(max_length=50)
	name = models.CharField(max_length=50)

class Choice(models.Model):
	question = models.ForeignKey(Question)
	choice = models.CharField(max_length=50)


class Answer(models.Model):
	question = models.ForeignKey(Question)
	name = models.CharField(max_length=50)


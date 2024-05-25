
from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models

#models: users, docs, workspaces, workspace_docs

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
 

 

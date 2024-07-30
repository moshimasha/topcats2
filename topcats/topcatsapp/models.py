
from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models
from datetime import date

#models: users, docs, workspaces, workspace_docs

'''
class Users(AbstractUser):
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20, blank=True)
    display_name = models.CharField(max_length=50)

class Groups(models.Model):
    display_name = models.CharField(max_length=50)

class Invites(models.Model):
    invitor = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='user_inviting')
    invited = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='user_invited')


class User_Groups(models.Model):
    userid = models.ForeignKey(Users, on_delete=models.CASCADE)
    groupid = models.ForeignKey(Groups, on_delete=models.CASCADE)

class Recipes(models.Model):
    name = models.CharField(max_length=200)
    display_image = models.ImageField()
    instructions = models.TextField()
    timestamp = models.DateTimeField()

class Recipe_Groups(models.Model):
    recipeid = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    groupid = models.ForeignKey(Groups, on_delete=models.CASCADE)
  
class Ingredients(models.Model):
    amount = models.CharField(max_length=10)
    amount_type = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    recipeid = models.ForeignKey(Recipes, on_delete=models.CASCADE)
 
 '''
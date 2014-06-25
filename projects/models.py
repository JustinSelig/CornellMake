from django.db import models

class Project(models.Model):
	user = models.CharField(max_length=100) #associate user(s) with project?
	name = models.CharField(max_length=100)
	organization = models.CharField(max_length=100)
	description = models.TextField(max_length=500)
	email = models.EmailField(max_length=100)
	image = models.CharField(max_length=200, default="http://www.placekitten.com/200/300/", null=True)

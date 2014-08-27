from django.db import models
from time import time
from django.contrib.auth.models import User

#""" Category model. A Category has an automatically-produced id and a name. """  
#class Category(models.Model):
#	category_id = models.AutoField(primary_key=True)
#	category = models.CharField(max_length=25)

def get_upload_file_name(instance, filename):
	return "images/project_submissions/uploaded_files/%s_%s" % (str(time()).replace('.','_'), filename)

class ProjectSubmission(models.Model):
	name = models.CharField(max_length=100) #person's name
	email = models.EmailField(max_length=100)
	organization = models.CharField(max_length=100, null=True)
	website = models.CharField(max_length=100, null=True)
	idea_name = models.CharField(max_length=500, null=True) #project's name
	description = models.TextField(max_length=500, default='default')
	CATEGORY_CHOICES = (
		('PT','Project Team'),
		('RESEARCH', 'Research'),
		('STARTUP', 'Startup'),
		('CH', 'Computer Hardware'),
		('CS', 'Computer Software'),
		('MECHE', 'Mechanical'),
		('ENV', 'Environmental'),
		('ADM', 'Art, Design, or Multimedia'),
		('SE', 'Social Entrepreneurship'),
		('OTHER', 'Other'),
	)
	category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, null=True)
	image = models.FileField(upload_to=get_upload_file_name, default="Image")
	url = models.SlugField(max_length=200, null=True, unique=True)
	owner = models.ForeignKey(User, null=True)
	
class Project(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField(max_length=100)
	organization = models.CharField(max_length=100, null=True)
	website = models.CharField(max_length=100, null=True)
	idea_name = models.CharField(max_length=500, null=True)
	description = models.TextField(max_length=500, default='default')
	category = models.CharField(max_length=10, null=True)
	image = models.FileField(upload_to=get_upload_file_name, default="Image")
	url = models.SlugField(max_length=200, null=True, unique=True)
	owner = models.ForeignKey(User, null=True)
	member_requests = models.ManyToManyField(User, related_name='member_requests')
	members = models.ManyToManyField(User, related_name='members')

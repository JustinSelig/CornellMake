from django.db import models

""" Category model. A Category has an automatically-produced id and a name. """  
class Category(models.Model):
	category_id = models.AutoField(primary_key=True)
	category = models.CharField(max_length=25)

def get_upload_file_name(instance, filename):
	return "uploaded_files/%s_%s" % (str(time()).replace('.','_'), filename)

class Project(models.Model):
	name = models.CharField(max_length=100)
	organization = models.CharField(max_length=100, null=True)
	description = models.TextField(max_length=500, default='default')
	email = models.EmailField(max_length=100)
	image = models.FileField(upload_to=get_upload_file_name, default="http://www.placekitten.com/200/300/")
	category = models.ForeignKey(Category, null=True)
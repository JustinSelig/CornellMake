from django.db import models

class Event(models.Model):
	day = models.IntegerField(null=True, default=1)
	month = models.IntegerField(null=True, default=1)
	year = models.IntegerField(null=True, default=1)
	name = models.CharField(max_length=100)
	description = models.TextField(max_length=500)
	image = models.CharField(max_length=200, default="http://www.placekitten.com/200/300/", null=True)
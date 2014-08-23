from django.db import models
from django.contrib.auth.models import User
from projects.models import Project

#store all the profle information in this class
class UserProfile(models.Model):
	user = models.OneToOneField(User)
	username = models.CharField(max_length=100, default='username')
	projects = models.ManyToManyField(Project)
#	join_requests = ...
	

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
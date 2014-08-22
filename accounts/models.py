from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	username = models.CharField(max_length=100, default='username')

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
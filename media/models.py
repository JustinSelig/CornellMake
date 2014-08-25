from django.db import models

# Create your models here.

class MediaObject(models.Model):
    name = models.CharField()
    upload_date = models.DateField()
    media_types = (
        ('image', 'Image'),
        ('video', 'Video')
        )
    type = models.CharField(max_length = 5,
                            choices=media_types,
                            default=image)
    description = models.TextField()
    image = models.ImageField(upload_to = "images/media", null = True)
    video = models.SlugField(null = True)

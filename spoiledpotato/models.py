from django.db import models

# Create your models here.

class Actor(models.Model):
    name = models.CharField(max_length=100)
    birthday = models.CharField(max_length=100)
    about = models.TextField()
    photo_url = models.TextField()

    def __str__(self):
        return self.name
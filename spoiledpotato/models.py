from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Actor(models.Model):
    name = models.CharField(max_length=100)
    birthday = models.DateField()
    about = models.TextField()
    photo_url = models.TextField()

    def __str__(self):
        return self.name
    
class Movie(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE, related_name='movies')
    title = models.CharField(max_length=100)
    length = models.DurationField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    preview_url= models.TextField()

    def __str__(self):
        return self.title 

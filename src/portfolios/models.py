from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    video = models.CharField(max_length=60)

class Event(models.Model):
    title = models.CharField(max_length=120)
    date = models.DateField()
    description = models.TextField()

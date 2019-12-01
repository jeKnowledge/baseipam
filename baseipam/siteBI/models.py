from django.db import models

# Create your models here.
class Content(models.Model):
    pt_content = models.TextField("Texto Português:")
    eng_content = models.TextField("Texto Inglês:")
    identifier = models.CharField(max_length=30)
    

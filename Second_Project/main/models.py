from django.db import models

# Create your models here.

class Entry(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=100)


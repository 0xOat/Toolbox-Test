from django.db import models

# Create your models here.
class Book(models.Model):
    id = models.IntegerField(primary_key=True,unique=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
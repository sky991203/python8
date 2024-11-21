from django.db import models
from django.utils import timezone

# Create your models here.
class Address(models.Model):
    name = models.CharField(max_length=200)
    addr = models.TextField()
    rdate = models.DateTimeField()
    
class Board(models.Model):
    writer = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=500)
    content = models.TextField() 
    rdate = models.DateTimeField(default=timezone.now)

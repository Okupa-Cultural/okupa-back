from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    mail = models.EmailField()
    start_date = models.DateField()
    bio = models.TextField(null=True, blank=True)

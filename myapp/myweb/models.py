from django.db import models

# Create your models here.
class Users(models.Model):
    title=models.CharField(max_length=150)
    body=models.TextField()
    timestart=models.DateTimeField()

class music(models.Model):
    title_name=models.TextField()
    num=models.TextField()
    link=models.TextField()
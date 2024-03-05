from django.db import models

# Create your models here


class Jobs(models.Model):
    post =models.CharField(max_length=100)
    exp = models.IntegerField()
    qual =models.CharField(max_length=100)
    last_date = models.DateField()
    description = models.TextField()

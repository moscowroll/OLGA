from django.db import models

# from Gogo.Gogo import settings


class Person(models.Model):
    name = models.CharField(max_length = 20)
    birth_date = models.DateField()
    gender = models.CharField(max_length = 10)
# Create your models here.

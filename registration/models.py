from django.db import models

# from Gogo.Gogo import settings
from datetime import datetime


class Question_1(models.Model):
    choice_1 = models.IntegerField()

class Question_2(models.Model):
    choice_1 = models.IntegerField()



class Person(models.Model):
    name = models.CharField(max_length = 20)
    age = models.IntegerField()
    gender = models.CharField(max_length = 10)

    login = models.CharField(max_length=20, default='cock', unique= True)

    last_login =  models.DateTimeField(default=datetime.now)
    date_joined =   models.DateTimeField(default=datetime.now)


    answer_1 = models.ForeignKey(Question_1, default = 3, on_delete = models.CASCADE)
    answer_2 = models.ForeignKey(Question_2, default = 4, on_delete = models.CASCADE)

# Create your models here.

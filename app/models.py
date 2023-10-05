from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    marks = models.CharField(max_length=100)

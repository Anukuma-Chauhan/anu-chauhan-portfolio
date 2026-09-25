from django.db import models

# Create your models here.
class Doctors(models.Model):
    name = models.CharField(max_length=30)
    contact = models.IntegerField()
    email = models.EmailField(max_length=30)

from django.db import models

# Create your models here.
class Employee(models.Model):
    Name=models.CharField(max_length=200)
    Email=models.EmailField(max_length=200)
    Age=models.CharField(max_length=100)
    Department=models.CharField(max_length=200)
    Location=models.CharField(max_length=200)

    
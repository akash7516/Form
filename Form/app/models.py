from django.db import models

# Create your models here.
class Signup(models.Model):

    email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=10)
    password=models.CharField(max_length=50)
    age=models.CharField(max_length=2)
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class Form1(models.Model):
    area=models.CharField(max_length=50)
    t_person=models.IntegerField()
    leads=models.CharField(max_length=50) 
    def __str__(self):
        return self.area  

class Form2(models.Model):
    name=models.CharField(max_length=50)
    dob=models.CharField(max_length=10)
    age=models.CharField(max_length=2) 
    gender=models.CharField(max_length=6) 
    members=models.CharField(max_length=4) 
    def __str__(self):
        return self.name         
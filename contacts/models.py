from django.db import models
from django.shortcuts import render
from datetime import datetime

# Create your models here.
class Contact(models.Model):
    first_name =models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    car_id = models.IntegerField()
    customer_need =models.CharField(max_length=100)
    car_title = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    user_id = models.IntegerField(blank=True)
    created_date = models.DateTimeField(blank= True, auto_now_add=True)

    def __str__(self):
        return self.first_name


class ContactModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField()
    created_date = models.DateTimeField(default=datetime.now())
    
    def __str__(self):
        
        return self.name



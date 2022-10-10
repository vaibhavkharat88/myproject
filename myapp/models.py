from django.db import models

# Create your models 
class Contact(models.Model):
    city=models.CharField(max_length=20)
    phone=models.CharField(max_length=10)
    state=models.CharField(max_length=20)
    zip=models.CharField(max_length=8)


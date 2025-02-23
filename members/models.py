from django.db import models
from datetime import datetime

# Create your models here.
class member(models.Model):
    
    name= models.CharField(max_length=254)
    gender=models.CharField(max_length=254)
    registerno= models.BigIntegerField()
    idno=models.CharField(max_length=254)
    aadharno=models.BigIntegerField()
    year=models.BigIntegerField()
    image = models.ImageField(upload_to="picture/", height_field=None, width_field=None, max_length=100)
class destinaton(models.Model):
    
    name= models.CharField(max_length=254)
    gender=models.CharField(max_length=254)
    registerno= models.BigIntegerField()
    idno=models.CharField(max_length=254)
    aadharno=models.BigIntegerField()
    year=models.CharField(max_length=254)
    image = models.ImageField(upload_to="picture/", height_field=None, width_field=None, max_length=100)
   
class od_form(models.Model):
    name= models.CharField(max_length=254)
    idno= models.CharField(max_length=254)
    department_name= models.CharField(max_length=254)
    type_of_od= models.CharField(max_length=254)
    reason= models.CharField(max_length=254)
    duration= models.BigIntegerField()
    class_incharge_name= models.CharField(max_length=254)
    staff_id= models.CharField(max_length=254)
    
    

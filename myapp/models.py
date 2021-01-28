from __future__ import unicode_literals  
from django.db import models

# Create your models here.
class workers(models.Model):  
    first_name = models.CharField(max_length=30)  
    last_name = models.CharField(max_length=30) 
    mail_id=models.EmailField(max_length=30)
    entrydate = models.DateField()  
    age = models.IntegerField() 
    contact = models.IntegerField()  
     
class Meta:
    db_table="workers"
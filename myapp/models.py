from django.db import models

# Create your models here.
class workers(models.Model):  
    first_name = models.CharField(max_length=30)  
    last_name = models.CharField(max_length=30) 
    mail_id=models.EmailField(max_length=30)
    entrydate = models.DateField()  
    age = models.IntegerField() 
    contact = models.IntegerField()   
   
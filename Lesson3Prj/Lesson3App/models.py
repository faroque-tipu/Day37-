from django.db import models
from datetime import datetime

# Create your models here.
class Student(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.EmailField(blank=True)
    dob=models.DateField(default=datetime.now,blank=True)

    def __str__(self):
        return "%s - %s - %s - %s" % (self.id,self.name,self.email,self.dob)
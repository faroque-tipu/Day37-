import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Lesson3Prj.settings')

import django
django.setup()

from Lesson3App.models import Student
from faker import Faker


from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


#pip install Faker
fakegen=Faker()

def addstudent():
     fake_name=fakegen.name()
     fake_email=fakegen.email()
     fake_dob=fakegen.date()

     Student.objects.get_or_create(name=fake_name,email=fake_email,dob=fake_dob)

def populatedata(n=10):
    for entry in range(n):
        addstudent()

def makesuperuser(un,pw,em,fn,ln):
    User.objects.get_or_create(
       
       username=un,
       password=make_password(pw),
       email=em,
       first_name=fn,
       last_name=ln,
       is_staff=True,
       is_superuser=True,
       is_active=True

    )






if __name__ == '__main__':


    try:
        makesuperuser('admin','4567','admin@gmail.com','masum','khan')
        print ('super user created')
        print(50*'=')
    except:
        print('super user already exst')


    populatedata()
    
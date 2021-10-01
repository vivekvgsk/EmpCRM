from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class MyEmp(AbstractUser):
    phone=models.CharField(max_length=15,unique=True)
    gender_options=(("Male","Male"),
             ("Female","Female"),
             ("Others","Others"))
    gender=models.CharField(max_length=10,choices=gender_options,default="Male")
    image = models.ImageField(upload_to="images")

    doj=models.DateField(default="2021-10-30")
    address = models.CharField(max_length=100)
    department=models.CharField(max_length=50)

    def __str__(self):
       return self.department






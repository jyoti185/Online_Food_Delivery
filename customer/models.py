from django.db import models
from Admin1.models import CityModel
from vender.models import FoodItemsModel

class CustomerRegistrationModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    contact= models.IntegerField(unique=True)
    adress = models.TextField()
    city=models.ForeignKey(CityModel,on_delete=models.CASCADE)
    password=models.CharField(max_length=20)
    otp=models.IntegerField()


class OrderModel(models.Model):
    id = models.AutoField(primary_key=True)
    items=models.ManyToManyField(FoodItemsModel)
    quantity=models.IntegerField()
    total=models.FloatField()
    status=models.CharField(max_length=50)
    date=models.DateField(auto_now_add=True)
    adress=models.TextField()


# Create your models here.

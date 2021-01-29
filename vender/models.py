from django.db import models
from Admin1.models import CuisineModel,CityModel


class VenderRegistrationModel(models.Model):
    id=models.AutoField(primary_key=True)
    stall_name=models.CharField(max_length=200)
    contact_1=models.IntegerField(unique=True)
    contact_2=models.IntegerField(unique=True)
    cuisine_type=models.ForeignKey(CuisineModel,on_delete=models.CASCADE)
    photo=models.ImageField(upload_to='vender_images/')
    adress=models.TextField()
    vender_city=models.ForeignKey(CityModel,on_delete=models.CASCADE)
    password=models.CharField(max_length=20)
    otp=models.IntegerField()
    status=models.CharField(max_length=100)



class FoodTypeModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    vender_id=models.ForeignKey(VenderRegistrationModel,on_delete=models.CASCADE)
    status=models.CharField(max_length=50)


class FoodItemsModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    food_type=models.ForeignKey(FoodTypeModel,on_delete=models.CASCADE)
    price=models.FloatField()
    photo=models.ImageField(upload_to='fooditem_image/')



# Create your models here.

from django.db import models

class StateModel(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200,unique=True)
    photo=models.ImageField(upload_to='state_images/')

class CityModel(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, unique=True)
    photo = models.ImageField(upload_to='city_images/')
    city_state=models.ForeignKey(StateModel,on_delete=models.CASCADE)

class CuisineModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, unique=True)
    photo = models.ImageField(upload_to='cuisine_images/')



# Create your models here.

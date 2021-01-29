# Generated by Django 3.1.2 on 2021-01-29 04:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Admin1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VenderRegistrationModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('stall_name', models.CharField(max_length=200)),
                ('contact_1', models.IntegerField(unique=True)),
                ('contact_2', models.IntegerField(unique=True)),
                ('photo', models.ImageField(upload_to='vender_images/')),
                ('adress', models.TextField()),
                ('password', models.CharField(max_length=20)),
                ('otp', models.IntegerField()),
                ('status', models.CharField(max_length=100)),
                ('cuisine_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin1.cuisinemodel')),
                ('vender_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin1.citymodel')),
            ],
        ),
        migrations.CreateModel(
            name='FoodTypeModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=50)),
                ('vender_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vender.venderregistrationmodel')),
            ],
        ),
        migrations.CreateModel(
            name='FoodItemsModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('photo', models.ImageField(upload_to='fooditem_image/')),
                ('food_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vender.foodtypemodel')),
            ],
        ),
    ]

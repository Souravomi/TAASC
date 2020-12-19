from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BasicDetails(models.Model):
    Auth_Id = models.TextField(primary_key=True,max_length=12)
    Type = models.CharField(max_length=20)
    Name = models.CharField(max_length=50)
    House = models.CharField(max_length=100)
    Parish = models.CharField(max_length=50)
    Village = models.CharField(max_length=50)
    Panch_Muns = models.CharField(max_length=50)
    District = models.CharField(max_length=20)
    Phone = models.CharField(max_length=15)
    Email = models.CharField(max_length=50)
    Occupation = models.CharField(max_length=30)
    Farming = models.CharField(max_length=5)
    Rubber = models.CharField(max_length=5)
    DomesticAnimals = models.CharField(max_length=5)
    VegFru = models.CharField(max_length=5)
    Fish = models.CharField(max_length=5)
    Created_Date = models.DateField()

class FamilyMembers(models.Model):
    Auth_Id = models.ForeignKey(BasicDetails,on_delete=models.CASCADE)
    Name = models.CharField(max_length=50)
    Relationship = models.CharField(max_length=15)
    Blood = models.CharField(max_length=5)
    Job = models.CharField(max_length=20)
    Phone = models.CharField(max_length=15)

class DomesticAnimals(models.Model):
    Auth_Id = models.ForeignKey(BasicDetails,on_delete=models.CASCADE)
    Category = models.CharField(max_length=20)
    Count = models.CharField(max_length=10)
    Income = models.CharField(max_length=10)
    Marketing = models.CharField(max_length=20)
    Weed = models.CharField(max_length=5)
    More_Space = models.CharField(max_length=5)
    More_Intrest = models.CharField(max_length=5)

class VegFru(models.Model):
    Auth_Id = models.ForeignKey(BasicDetails,on_delete=models.CASCADE)
    Category = models.CharField(max_length=20)
    Land_Area = models.CharField(max_length=10)
    Income = models.CharField(max_length=10)
    Marketing = models.CharField(max_length=20)
    Weed = models.CharField(max_length=5)
    More_Space = models.CharField(max_length=5)
    More_Intrest = models.CharField(max_length=5)

class Fish(models.Model):
    Auth_Id = models.ForeignKey(BasicDetails,on_delete=models.CASCADE)
    Category = models.CharField(max_length=20)
    Land_Area = models.CharField(max_length=10)
    Method = models.CharField(max_length=15)
    Income = models.CharField(max_length=10)
    Marketing = models.CharField(max_length=20)
    More_Space = models.CharField(max_length=5)
    More_Intrest = models.CharField(max_length=5)

class Rubber(models.Model):
    Auth_Id = models.ForeignKey(BasicDetails,on_delete=models.CASCADE)
    Land_Area = models.CharField(max_length=10)
    Count = models.CharField(max_length=10)
    Income = models.CharField(max_length=10)
    Rubber_Sheet = models.CharField(max_length=20)
    Rubber_Board = models.CharField(max_length=5)

class Survey(models.Model):
    Auth_Id = models.ForeignKey(BasicDetails,on_delete=models.CASCADE)
    Intrest = models.CharField(max_length=5)
    Jobs = models.CharField(max_length=110)
    Business = models.CharField(max_length=110)
    News_Paper = models.CharField(max_length=50)

class Contact(models.Model):
    Auth_Name = models.CharField(max_length=30)
    Name = models.CharField(max_length=40)
    Email = models.CharField(max_length=40)
    Phone = models.CharField(max_length=15)
    Message = models.CharField(max_length=50)
    Date = models.DateField()
    Status = models.CharField(max_length=10)
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.
Months = [
    ("Jan", "January"),
    ("Feb", "Feburary"),
    ("Mar", "March"),
    ("Apr", "April"),
    ("May", "May"),
    ("Jun", "June"),
    ("Jul", "July"),
    ("Aug", "August"),
    ("Sep", "September"),
    ("Oct", "October"),
    ("Nov", "November"),
    ("Dec", "December"),
]

class Seed(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING) #not on_delete
    date_posted = models.DateField(default = timezone.now)
    seedName = models.CharField(max_length=50)
    content = models.TextField()
    seedImg = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    obtainTime = models.CharField(max_length=3, choices=Months, default="Jan")
    plantImg = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None, default='default.jpg')
    growthRate = models.IntegerField(null=False, default = 0)
    edibleFruit = models.BooleanField(null=False, default = False)

    def __str__(self) -> str:
        return self.seedName

class Step(models.Model):
    img = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None, default='default.jpg')
    content = models.TextField()
    seed = models.ForeignKey("seed.Seed", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.seed.seedName} step'

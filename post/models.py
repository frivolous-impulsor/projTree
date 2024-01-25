from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
# Create your models here.

Months = [
    ("Jan", "January"),
    ("SO", "Sophomore"),
    ("JR", "Junior"),
    ("SR", "Senior"),
    ("GR", "Graduate"),
]
class Seed(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING) #not on_delete
    seedName = models.CharField(max_length=50)
    seedImg = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    obtainTime = models.CharField(max_length=3, choices=Months, default="Jan")
    plantImg = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    growthRate = models.IntegerField()
    edibleFruit = models.BooleanField()

class Step(models.Model):
    seed = models.ForeignKey(Seed, on_delete=models.CASCADE)
    img = models.ImageField()
    description = models.TextField()


class Post(models.Model):
    title = models.CharField(max_length=50)
    img = models.ImageField() #to be specified
    content = models.TextField()
    year = models.CharField(max_length=3, choices = Months, default="FR")
    date_posted = models.DateField(default = timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} Post'
    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
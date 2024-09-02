

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')

    def __str__(self):
        return self.name



class Movie(models.Model):


    title=models.CharField(max_length=250,unique=True)

    image=models.ImageField(upload_to='poster',blank=True)
    description=models.TextField(blank=True)
    release_date=models.DateField(blank=True)
    actors=models.CharField(max_length=200,unique=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    trailer_link=models.URLField(max_length=250,unique=True)


    def __str__(self):
        return self.title
class Review(models.Model):
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE,related_name='reviews')
    photo = models.ImageField(upload_to='pho', blank=True)
    rating=models.IntegerField(default=1)
    comment=models.TextField()

    def __str__(self):
        return self.comment
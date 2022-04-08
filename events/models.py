from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Spekar(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField()
    title = models.CharField(max_length=200,blank=True,null=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=200)
    discption = RichTextField()
    location = models.CharField(max_length=200)
    date = models.DateTimeField()
    spekars = models.ManyToManyField(Spekar)
    image  = models.ImageField()

    def __str__(self):
        return self.name
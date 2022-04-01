from tkinter.tix import Tree
from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse


class Course(models.Model):
    instructor = models.ForeignKey("Instructor",on_delete=models.CASCADE)
    title = models.CharField(max_length=200,verbose_name="Course Title")
    category = models.CharField(max_length=200,blank=True,null=True)
    description = models.CharField(max_length=200,verbose_name="Course Description")
    content = RichTextField()
    image = models.ImageField()
    price = models.CharField(max_length=200,verbose_name="Course Price")
    discount_price = models.CharField(max_length=200,verbose_name="Course Discount Price")
    lesson = models.IntegerField(default=0)
    durantion = models.CharField(max_length=200,verbose_name="Durantion Course")
    best_seller = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('course_detail', kwargs={'course_detail': self.pk})




class Instructor(models.Model):
    fullname = models.CharField(max_length=200,verbose_name="Full Name")
    image = models.ImageField()
    position = models.CharField(max_length=200,verbose_name="Instructor position")
    description = RichTextField()


    def __str__(self):
        return self.fullname


class About_Course(models.Model):
    course = models.ForeignKey(Course,verbose_name="About Course",related_name="about_course",on_delete=models.CASCADE)
    title = models.CharField(max_length=200,verbose_name="Title")
    description = models.ManyToManyField("Description")

    def __str__(self):
        return self.title

class Description(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
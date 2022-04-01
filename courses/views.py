from django.shortcuts import render
from .models import Course
# Create your views here.

def courses(request):
    course = Course.objects.all()
    context = {'courses':course}
    template = "course-list-v1.html"
    return render(request,template,context)



def course_detail(request,id):
    course = Course.objects.get(id=id)
    template_name = "course-single-v2.html"
    context = {'course':course}
    return render(request,template_name,context)
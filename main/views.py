from django.shortcuts import render
from courses.models import Course
# Create your views here.
def home(request):
    course = Course.objects.all()
    template_name = "home-v5.html"
    context = {'course': course}
    return render (request, template_name,context)
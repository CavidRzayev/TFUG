from django.shortcuts import render
from courses.models import Course
from events.models import Event
def home(request):
    events = Event.objects.all()
    course = Course.objects.all()
    template_name = "home-v5.html"
    context = {'course': course,"events":events}
    return render (request, template_name,context)
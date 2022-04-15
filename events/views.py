from django.shortcuts import render
from .models import Event
# Create your views here.


def event_detail(request,id):
    event = Event.objects.get(id=id)
    template = "event-single.html"
    context = {"event":event}
    return render(request,template,context)

def event_list(request):
    events = Event.objects.all()
    template = "event-list.html"
    context = {"event":events}
    return render(request,template,context)

from django.urls import path
from .views import *
urlpatterns = [
    path('event/',event_list,name="event"),
    path('event/<int:id>/',event_detail,name="event_detail")
]
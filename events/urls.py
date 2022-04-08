from django.urls import path
from .views import *
urlpatterns = [
    path('event/<int:id>/',event_detail,name="event_detail")
]
from django.urls import path
from .views import *
urlpatterns = [
    path('courses/', courses,name='courses'),
    path('courses/<int:id>/',course_detail,name="course_detail")
]
from django.urls import path
from .views import *


app_name = "course"
urlpatterns = [
    path('python_course', python_course, name="python_course"),
    path('register', register, name="register"),
]
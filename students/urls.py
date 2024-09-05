from django.urls import path

from students.views import home, students


urlpatterns = [
    path("", home, name="home"),
    path("students/", students, name="students")
]

from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1> Hello from Home </h1>")


def students(request):
    return HttpResponse("<h1> Hi, these are the students from PLP </h1>")

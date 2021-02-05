from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("<h1 style='text=center'>Home!</>")

def hello(request):
    return HttpResponse("<h1 style='text=center'>Hello, World!</>")
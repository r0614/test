from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse
import operator
def home(requests):
    return HttpResponse('<h1> This is first page</h1>')
def about(requests):
    return HttpResponse('<h1> This is about</h1>')
def hobbies(requests):
    return HttpResponse('<h1> This is hobbies</h1>')
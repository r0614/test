from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse
import operator
def home(requests):
    return HttpResponse('<h1> This is first page</h1>')
def about(requests):
    return HttpResponse('<h1>ABOUT</h1><ul><li> This is about me</li><li> Im Renu Aakanksha from Vasavi College of Engineering</li></ol>')
def hobbies(requests):
    return HttpResponse('<h1> THESE ARE MY HOBBIES</h1><ul><li> I like to sing</li><li> I like to paint</li></ol>')
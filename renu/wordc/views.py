from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(requests):
   return render(requests,'wordc/home.html')
def aboutus(requests):
   return render(requests,'wordc/about.html')
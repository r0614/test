from django.shortcuts import render
from django.http import HttpResponse
import operator

# Create your views here.

def drinks(requests):
    return HttpResponse('Drinkign 3 L of water everyday will keep you healthy')
def foods(requests):
    return HttpResponse('Do not eat junk food, it is hamrful')
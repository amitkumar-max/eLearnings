from django.shortcuts import render
from django.http import HttpResponse

def payment_home(request):
    return HttpResponse("Payments Home Page")

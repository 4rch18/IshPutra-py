__author__ = 'arg0n1x'
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def camps(request):
    return render(request, 'camps.html')

def services(request):
    return render(request, 'services.html')

def literature(request):
    return render(request, 'literature.html')

def contact_us(request):
    return render(request, 'contact_us.html')
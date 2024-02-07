from django.shortcuts import render
from .models import Hospital


def home(request):
    hospitals = Hospital.objects.all()
    return render (request,'hospital/home.html',{
        'hospitals':hospitals
    })

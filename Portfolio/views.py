from django.http import HttpResponse
from django.shortcuts import render
from service.models import Service
def ABOUT(request):
    data={
         'title':'portfolio'
    }
    return render(request,"about.html",data)
def CONTACT(request):
    return render(request,"contact.html")


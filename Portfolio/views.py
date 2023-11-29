from django.http import HttpResponse
from django.shortcuts import render
def ABOUT(request):
    data={
         'title':'portfolio'
    }
    return render(request,"about.html",data)

def CONTACT(request):
    return render(request,"contact.html")

def GALLARY(request):
    return render(request,"gallery-single.html")

def login(request):
    return render(request,"gallery.html")

def GALLARY(request):
    return render(request,"sample-inner-page.html")

def HOME(request):
    return render(request,"index.html")

def SERVICE(request):
    return render(request,"services.html")

def UPDATE(request):
    return render(request,"gallery.html")

    

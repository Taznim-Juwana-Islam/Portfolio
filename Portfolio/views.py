from django.http import HttpResponse
from django.shortcuts import render
from Service.models import Service

def ABOUT(request):
    data={
         'title':'portfolio'
    }
    return render(request,"about.html",data)

def CONTACT(request):
    return render(request,"contact.html")

def saveEnquiry(request):
    n=''
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        message=request.POST.get('message')
        data=Service(title=name,description=email,date=phone,status=message)
        data.save()
        n='data inserted'

    return render(request,"contact.html",{'n':n})

def GALLARY(request):
    return render(request,"gallery-single.html")

def login(request):
    return render(request,"gallery.html")

def saveEnquiry1(request):
    n=''
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        data=Service(title=email,description=password)
        data.save()
        n='data inserted'

    return render(request,"gallery.html",{'n':n})

def GALLARY(request):
    return render(request,"sample-inner-page.html")
   
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

    
def SERVICE(request):
    return render(request,"services.html")

def UPDATE(request):
    return render(request,"gallery.html")

    
from django.http import HttpResponse
from django.shortcuts import render,HttpResponse
from myapp.models import Contact
# Create your views here.

def home(request):
    return  render(request,'home.html')

def about(request):
    return render(request,'about.html')
def contact(request):
    if request.method=="POST":
        city=request.POST['city']
        phone=request.POST['phone']
        state=request.POST['state']
        zip=request.POST['zip']
        info=Contact(city=city,phone=phone,state=state,zip=zip)   
        info.save()
        print("data is giong to db")
    return render(request,'contact.html')
def services(request):

    return render(request,'services.html')
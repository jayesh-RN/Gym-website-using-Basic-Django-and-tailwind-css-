from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context={
        'variable': "Harry is great"
    }
    messages.success(request, "this is a test message")
    return render(request,'index.htm',context)
    #return HttpResponse("this is homepage")

def about(request):
    # return HttpResponse("this is about page")
    return render(request,'about.htm')

def services(request):
    # return HttpResponse("this is services page")
    return render(request,'services.htm')

def contact(request):
    # return HttpResponse("this is contact page")
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        city = request.POST.get('city')
        state = request.POST.get('state')
        phone = request.POST.get('phone')
        contact = Contact(name=name,email=email,city=city,state=state,phone=phone,date=datetime.today())
        contact.save()
        messages.success(request, 'your message has been sent!')
    return render(request,'contact.htm')
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_view(request,*args, **kwargs):
    print(args,kwargs)
    print(request.user)
    return render(request,'home.html',{})

def contacts_view(request,*args, **kwargs):
    return render(request,'contact.html',{})

def about_view(request,*args, **kwargs):
    my_context = {
        "my_text":"this is my text",
        "my_number":123,
        "my_list":[1,2,3,4]
    }
    return render(request,'about.html',my_context)    
from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
import random

def index(request):
    return render(request, 'index.html')

def new(request):
    return render(request, 'new.html')

def create(request):
    print("You created a blog post")
    return redirect('/')

def show(request, number):
    context = {
        'blog_id': number,
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime()),
    }
    return render(request, 'time_display.html', context)


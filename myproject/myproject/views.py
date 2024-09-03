# from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # return HttpResponse("First django project, I'm home.")
    return render(request, 'home.html')

def about(request):
    # return HttpResponse("Django project, my about page")
    return render(request, 'about.html')

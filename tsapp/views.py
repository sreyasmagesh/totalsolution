from django.shortcuts import render

def home(request):
    return render(request,'home.html')


def login(request):
    return render(request,'login.html')

def explore(request):
    return render(request,'explore.html')

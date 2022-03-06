from django.http import HttpResponse
from django.shortcuts import render,HttpResponse,render

# Create your views here.

def home(request):
    return render(request,'main/index.html')

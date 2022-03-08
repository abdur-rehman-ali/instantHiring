from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render,HttpResponse,render
from .forms import registrationForm

# Create your views here.

def home(request):
    return render(request,'main/index.html')


def register(request):
    if request.method == "POST":
        form = registrationForm(request.POST)
        if form.is_valid():
            form.save()
            form = registrationForm()
    else:
        form = registrationForm()
    template_name = 'main/register.html'
    context={
        'form':form
    }
    return render(request,template_name,context)

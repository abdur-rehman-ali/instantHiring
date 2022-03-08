from django.contrib.auth import login,authenticate,logout
from django.shortcuts import render,HttpResponseRedirect
from .forms import registrationForm,logInForm

# Create your views here.

def home(request):
    return render(request,'main/index.html')


def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
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


def logIn(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
        if request.method=="POST":
            fm=logInForm(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect('/')
        else:        
            fm=logInForm()
        template_name = 'main/logIn.html'
        context = {
            'form':fm
        }
        return render(request,template_name,context)

def logOut(request):
    logout(request)
    return HttpResponseRedirect('logIn')
    

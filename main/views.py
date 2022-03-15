from multiprocessing import context
from django.contrib.auth import login,authenticate,logout
from django.shortcuts import render,HttpResponseRedirect
from .forms import registrationForm,logInForm,userDataUpdateForm,PostForm
from .models import jobPostData
from django.urls import reverse_lazy

# Create your views here.

def home(request):

    data = jobPostData.objects.all()
    template_name = 'main/index.html'
    context={
        'data':data,
    }
    return render(request,template_name,context)



def jobPost(request):
    form = PostForm()
    template_name = 'main/jobPost.html'
    context={
        'form':form
    }
    return render(request,template_name,context)

def jobPost(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=PostForm(request.POST)
            if fm.is_valid():
                postTitle = fm.cleaned_data['title']
                desription = fm.cleaned_data['desription']
                location = fm.cleaned_data['location']
                job_nature = fm.cleaned_data['job_nature']
                vacancy = fm.cleaned_data['vacancy']
                salary = fm.cleaned_data['salary']
                application_deadline = fm.cleaned_data['application_deadline']
                postAuthor = request.user.username
                post = jobPostData(title=postTitle,desription=desription,application_deadline=application_deadline,salary=salary,location=location,job_nature=job_nature,vacancy=vacancy,author=postAuthor,user_job_post_id=request.user.id)
                post.save()
                fm=PostForm()
        else:       
            fm=PostForm()
        template_name = 'main/jobPost.html'
        context={
        'form':fm
        }
        return render(request,template_name,context)

    else:
        return HttpResponseRedirect('/logIn')


def jobPostDetail(request,id):
    data = jobPostData.objects.get(id=id)
    template_name = 'main/jobPostDetail.html'
    context={
        'data':data
    }
    return render(request,template_name,context)


def jobPostUpdate(request,id):
    if request.user.is_authenticated:
        post=jobPostData.objects.get(pk=id)
        if request.method=="POST":
            fm=PostForm(request.POST,instance=post)
            if fm.is_valid():
                fm.save()
        else:
            fm = PostForm(instance=post)
        template_name = 'main/updatePost.html'
        context ={
            'form':fm
        }
        return render(request,template_name,context)
    else:
        return HttpResponseRedirect('/logIn')

def jobPostDelete(request,id):
    if request.user.is_authenticated:
        post=jobPostData.objects.get(id=id)
        post.delete()
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/logIn')


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


def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm=userDataUpdateForm(data=request.POST,instance=request.user)
            if fm.is_valid():
                fm.save()
        else:
            fm=userDataUpdateForm(instance=request.user)
        template_name = 'main/profile.html'
        context={
            'form':fm
        }
        return render(request,template_name,context)
    else:
        return HttpResponseRedirect('/logIn')


def logOut(request):
    logout(request)
    return HttpResponseRedirect('/logIn')
    

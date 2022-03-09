from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('logIn',views.logIn,name='logIn'),
    path('logOut',views.logOut,name='logOut'),
    path('profile',views.profile,name='profile'),
]

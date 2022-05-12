from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('job_post',views.jobPost,name='jobPost'),
    path('job_post_detail/<int:id>',views.jobPostDetail,name='jobPostDetail'),
    path('job_post_update/<int:id>',views.jobPostUpdate,name='jobPostUpdate'),
    path('job_post_delete/<int:id>',views.jobPostDelete,name='jobPostDelete'),
    path('register',views.register,name='register'),
    path('student_register',views.studentRegister,name='studentRegister'),
    path('company_register',views.companyRegister,name='companyRegister'),
    path('logIn',views.logIn,name='logIn'),
    path('logOut',views.logOut,name='logOut'),
    path('profile',views.profile,name='profile'),
    path('update_profile',views.updateProfile,name='updateProfile'),
    path('student_profile_update/<int:id>',views.studentProfileUpdate,name='studentProfileUpdate'),
    path('student_profile_detail/<int:id>',views.studentProfileDetail,name='studentProfileDetail'),
]

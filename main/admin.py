from django.contrib import admin
from .models import jobPostData,StudentProfile

# Register your models here.

@admin.register(jobPostData)
class jobPostDataAdmin(admin.ModelAdmin):
    list_display = ['title','location','job_nature','category']

admin.site.register(StudentProfile)
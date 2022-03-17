from django.db import models
from django.contrib.auth.models import User
import datetime
from ckeditor.fields import RichTextField

# Create your models here.
class jobPostData(models.Model):
    CATEGORY_CHOICES = (
    ("Design & Creative", "Design & Creative"),
    ("Design & Development", "Design & Development"),
    ("Sales & Marketing", "Sales & Marketing"),
    ("Mobile Application", "Mobile Application"),
    ("Construction", "Construction"),
    ("Information Technology", "Information Technology"),
    ("Real Estate", "Real Estate"),
    ("Content Writer", "Content Writer"),
    )

    JOB_CHOICES =(
        ("Part Time","Part Time"),
        ("Full Time","Full Time"),
        ("Remote","Remote"),
        ("On site","On site"),
    )

    title = models.CharField(max_length=70,default='')
    desription = RichTextField(null=True,blank=True)
    author = models.CharField(max_length=50)
    location = models.CharField(max_length=100,default='')
    job_nature = models.CharField(max_length=30,choices=JOB_CHOICES,default='No choice')
    category = models.CharField(max_length=50,choices=CATEGORY_CHOICES,default='No category')
    posted_date = models.DateTimeField(auto_now_add=True)
    vacancy = models.IntegerField(default=1)
    salary = models.CharField(max_length=30,default='')
    application_deadline = models.DateTimeField(default=datetime.datetime.now())
    user_job_post = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"


class StudentProfile(models.Model):
    user = models.OneToOneField(to=User,on_delete=models.CASCADE,null=True)
    bio = models.CharField(max_length=70)
    facebook_url = models.CharField(max_length=70,null=True,blank=True)
    linkedin_url = models.CharField(max_length=70,null=True,blank=True)
    github_url = models.CharField(max_length=70,null=True,blank=True)
    instagram_url = models.CharField(max_length=70,null=True,blank=True)
    website_url = models.CharField(max_length=70,null=True,blank=True)
    profile_pic = models.ImageField(blank=True,null=True,upload_to='images/profile/')

    def __str__(self):
        return f"{self.bio}"
        
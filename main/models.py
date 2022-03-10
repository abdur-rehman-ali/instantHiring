from sre_constants import CATEGORY
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User

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

    title = models.CharField(max_length=70)
    desription = models.TextField()
    author = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    job_nature = models.CharField(max_length=30,choices=JOB_CHOICES,default='No choice')
    category = models.CharField(max_length=50,choices=CATEGORY_CHOICES,default='No category')
    date = models.DateTimeField(auto_now_add=True)
    user_job_post = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class jobPostData(models.Model):
    title = models.CharField(max_length=70)
    desription = models.TextField()
    author = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    job_nature = models.CharField(max_length=30)
    category = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    user_job_post = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"
from django.db import models
from accounts.models import Profile
# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200)
    description =  models.TextField()
    image = models.ImageField(upload_to='project_pics')
    link = models.CharField(max_length=200)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

class Technology(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    technology =  models.CharField(max_length= 300)

    def __str__(self):
        return self.technology

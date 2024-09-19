from django.db import models
from accounts.models import Profile
# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='project_pics')
    link = models.CharField(max_length=200)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    live_demo_link = models.CharField(null=True, max_length=300)
    def __str__(self):
        return self.title
    

class Overview(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    summary = models.TextField()
    problem_statement=models.TextField()

    def __str__(self):
        return f"Overview for {self.project.title}"

class Features(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    feature = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.feature

class Challanges(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    challenge = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.challenge

class Technology(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    technology =  models.CharField(max_length= 300)

    def __str__(self):
        return f'{self.technology} in {self.project.title}'
 

class Improvement(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    improvement = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.improvement
    
class Review(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    comment = models.TextField()
    rating = models.IntegerField()
    def __str__(self):
        return f"{self.name} - {self.rating} stars"
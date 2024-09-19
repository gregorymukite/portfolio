from django.db import models
from accounts.models import Account
# Create your models here.
class About(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    profesional_background = models.TextField()
    phone_number = models.CharField(null=True, max_length=20)
    email = models.EmailField(null = True)
    address = models.CharField(null = True, max_length=200)
    def __str__(self):
        return self.user.username

class Skill_Cartegory(models.Model):
    skill = models.CharField(max_length=100)
    def __str__(self):
        return self.skill
    
class Myskill(models.Model):
    PROFICIENCY_CHOICES = [
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
    ]
    name = models.CharField(max_length=100)
    proficiency = models.CharField(max_length=12, choices=PROFICIENCY_CHOICES)
    category = models.ForeignKey(Skill_Cartegory, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name} ({self.proficiency})"


class WorkExperience(models.Model):
    company_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.job_title
    
class Duties(models.Model):
    experience = models.ForeignKey(WorkExperience, on_delete=models.CASCADE)
    duties = models.CharField(max_length=400)
    def __str__(self):
        return self.duties
    
class Education(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    school_name = models.CharField(max_length=100)
    education_level = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    grade = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.school_name
    
    @property
    def start_year(self):
        return self.start_date.strftime('%Y')
    @property
    def end_year(self):
        return self.end_date.strftime('%Y')

class CourseWork(models.Model):
    course = models.ForeignKey(Education, on_delete=models.CASCADE)
    relevant_course_Work= models.CharField(max_length=210)
    description =models.TextField()
    def __str__(self):
        return self.relevant_course_Work

class Archievement(models.Model):
    school= models.ForeignKey(Education, on_delete=models.CASCADE)
    achievement_title = models.CharField(max_length=100)
    achievement_date = models.DateField(null= True, blank=True)
    description = models.TextField()
 
class PersonalIntrest(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    intrest = models.TextField(max_length=100)

class Services(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    service = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.service 
    

    
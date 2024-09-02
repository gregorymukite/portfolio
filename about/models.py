from django.db import models
from accounts.models import Account
# Create your models here.
class About(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    bio = models.TextField()
    profesional_background = models.TextField()


class PersonalDetails(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.phone_number
    
class Skills(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    skills = models.CharField(max_length=100)

    def __str__(self):
        return self.skills
class Skill_technologies(models.Model):
    skill = models.ForeignKey(Skills, on_delete=models.CASCADE)
    skill_tech = models.CharField(max_length=100)
    proficiency = models.IntegerField()

    def __str__(self):
        return self.skill_tech


class WorkExperience(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
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
    cerificate = models.CharField(max_length=100)
    grade = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.school_name
    
class PersonalIntrest(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    intrest = models.TextField(max_length=100)

class Services(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    service = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.service 
    

    
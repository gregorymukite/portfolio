from django.shortcuts import render, get_object_or_404
from .models import *
from projects.models import *
from home.models import Dashboard
# Create your views 
def about(request):
    about = About.objects.all()
    project = Project.objects.all()
    dashboard = Dashboard.objects.all()
    project = Project.objects.prefetch_related('overview_set').all()
    education = Education.objects.all()
    skills = Skill_Cartegory.objects.prefetch_related('myskill_set').all()
    context = {
        'about': about,
        'project': project,
        'dashboard': dashboard,
        'project': project,
        'education':education,
        'skills':skills,

    }
    return render(request, 'about/about.html', context)
def Skill(request):
    skills = Skill_Cartegory.objects.prefetch_related('myskill_set').all()
    context = {
       'skills': skills,   
    }
    return render(request, 'about/skills.html', context)


def service(request):
    myservices = Services.objects.all()
    context = {
        'myservices': myservices,   
    }
    return render(request, 'service/service.html', context)

def Education_Background(request, id):
    education = get_object_or_404(Education.objects.prefetch_related('coursework_set', 'archievement_set'), id=id) 
    context = {
        'education': education,   
    }
    return render(request, 'about/education.html', context)
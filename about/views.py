from django.shortcuts import render
from .models import *
from projects.models import *
from home.models import Dashboard
# Create your views 
def about(request):
    about = About.objects.all()
    project = Project.objects.all()
    dashboard = Dashboard.objects.all()
    project = Project.objects.all()
    education = Education.objects.all()
    skills = Skills.objects.all()
    context = {
        'about': about,
        'project': project,
        'dashboard': dashboard,
        'project': project,
        'education':education,
        'skills':skills,

    }
    return render(request, 'about/about.html', context)


def service(request):
    myservices = Services.objects.all()

    context = {
        'myservices': myservices,
        
    }

    return render(request, 'service/service.html', context)
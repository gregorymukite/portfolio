from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.
def ProjectDetails(request, id):
    project = get_object_or_404(Project.objects.prefetch_related('overview_set', 'technology_set').filter(id = id))
    context = {
        'project':project,
    }
    return render(request,'project/project_details.html', context)
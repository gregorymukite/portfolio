from django.shortcuts import render

# Create your views here.
def ProjectDetails(request):
    return render(request,'project/project_details.html')
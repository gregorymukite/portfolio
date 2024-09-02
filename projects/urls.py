from django.urls import path
from .views import ProjectDetails

urlpatterns = [
    path('', ProjectDetails, name = 'project_details'),
]

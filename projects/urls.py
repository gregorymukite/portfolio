from django.urls import path
from .views import ProjectDetails

urlpatterns = [
    path('project_details/<int:id>/', ProjectDetails, name = 'project_details'),
]

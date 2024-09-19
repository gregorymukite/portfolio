from django.urls import path, include
from .views import about, service, Education_Background, Skill
urlpatterns = [
    path('', about, name = "about"),
    path('about/', about, name = "about"),
    path('skills/', Skill, name = 'skills'),
    path('service/', service, name = "service"),
    path('education/<int:id>/', Education_Background, name="education"),
   
]
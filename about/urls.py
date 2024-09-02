from django.urls import path, include
from .views import about, service
urlpatterns = [
    path('', about, name = "about"),
    path('about/', about, name = "about"),
    path('service/', service, name = "service"),

]
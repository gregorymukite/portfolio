from django.shortcuts import render
from .models import *
from about.models import *
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
# Create your views here.
def home(request):
    about = About.objects.all()
    slide = SlideImage.objects.all()
    dashboard = Dashboard.objects.all()

    context = {
        'dashboard':dashboard,
        'about':about,
        'slide':slide,
    }
    return render(request, 'home/index.html', context)

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        send_mail(
            'Message from ' + name,
            message,
            email,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )
        messages.success(request, 'Your message has been sent successfully!')
        return render(request, 'contact/contact.html', {'name': name})
        
    else:
    
        return render(request, 'contact/contact.html')
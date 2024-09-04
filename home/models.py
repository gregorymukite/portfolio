from django.db import models
from accounts.models import Account,Profile
# Create your models here

class Dashboard(models.Model):
    intro = models.TextField()
    a_img1 = models.ImageField(upload_to='about_images', null=True)
    a_img2 = models.ImageField(upload_to='about_images', null = True)


class SlideImage(models.Model):
    image = models.ImageField(upload_to='images/')  # Ensure this path exists in your media directory
    alt_text = models.CharField(max_length=255, blank=True, null=True)
    text = models.CharField(max_length=250, blank=True, null=True)

   
class Testmonial(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    context = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.context
    
 
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    creaed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
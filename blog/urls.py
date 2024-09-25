from django.urls import path, include
from .views import Blog, create_blog_post,BlogDetails,create_comment
urlpatterns = [
    path('', Blog, name = "blog"),
    path('blog/', Blog, name = "blog"),
    path('blog_input/', create_blog_post, name = "blog_input"),
    path('blog_details/<int:id>/', BlogDetails, name = "blog_details"),
    path('blog/create_comment/', create_comment, name="create_comment"),
    
   
]
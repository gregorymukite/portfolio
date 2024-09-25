from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import *
from django.http import JsonResponse
from .models import BlogPost, BlogSection, Category,  Comment

# Create your views here.
def Blog(request):
    blog_posts =  BlogPost.objects.all()
    blog_sections= BlogSection.objects.all()
    category = Category.objects.all()

    context = {
        'blog_sections': blog_sections,  # For blog sections
        'blog_posts': blog_posts,  # For paginated blog posts
        'category': category,  # For all categories in the blog
    }
    
    return render(request, 'blog/blog.html', context)

def BlogDetails(request, id):
    blog_post = get_object_or_404(BlogPost.objects.prefetch_related('comment_set').filter(id = id))
    blog_sections= BlogSection.objects.filter(blog = blog_post)
    category = Category.objects.all()

    context = {
        'blog_sections': blog_sections,  # For blog sections
        'blog_posts': blog_post,  # For paginated blog posts
        'category': category,  # For all categories in the blog
    }
    
    return render(request, 'blog/blog_details.html', context)




def create_blog_post(request):
    if request.method == 'POST':
        # Extract the main BlogPost data
        title = request.POST.get('title')
        author= request.POST.get('author')
        category_id = request.POST.get('category')

        # Get the author and category from the database
        category = Category.objects.get(id=category_id) if category_id else None

        # Create the BlogPost object
        blog_post = BlogPost.objects.create(
            title=title,
            author=author,
            category=category,
        )

      

        # Save Blog Sections
        section_count = 1
        while True:
            section_type = request.POST.get(f'section_type_{section_count}')
            content = request.POST.get(f'content_{section_count}')

            if not section_type or not content:
                break

            # Create a new BlogSection object
            BlogSection.objects.create(
                blog=blog_post,
                section_type=section_type,
                content=content
            )

            section_count += 1

        # After saving all sections, redirect to a success page or the blog post
        return redirect('blog')  # or 'blog_detail' with the new post id

    # GET method to render the form

    
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'blog/blog_input.html', context)

def create_comment(request):
    if request.method == 'POST':
        blog_post_id = request.POST.get('blog_post_id')
        comment_text = request.POST.get('comment')
        blog_post = get_object_or_404(BlogPost, id = blog_post_id)
        name = request.POST.get('name')
        
        #create comment
        comment = Comment.objects.create(
            Blog = blog_post,
            author = name,
            comment = comment_text,
        )
        comment.save()
        return redirect('blog_details', id=blog_post_id)

        



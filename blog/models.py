from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
class BlogPost(models.Model):
    author = models.CharField(max_length=50)
    category=models.ForeignKey( Category, on_delete=models.CASCADE, null=True,)
    title = models.CharField(max_length=100)
    published_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class BlogSection(models.Model):
    SECTION_TYPE = [
        ('heading', 'Heading'),
        ('paragraph', 'Paragraph'),
        ('image', 'Image'),
        ('list', 'List'),
        ('quote', 'Quote'),
    ]
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    section_type = models.CharField(max_length=10, choices=SECTION_TYPE)
    content = models.TextField()
    order = models.IntegerField() 

    def save(self, *args, **kwargs):
        if self.order is None:
            last_number = BlogSection.objects.all().order_by('order').last()
            if last_number:
                self.order = last_number.order + 1
            else:
                self.order = 1
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.section_type} in {self.blog.title}'
    
    class Meta:
        ordering = ['order']

class Comment(models.Model):
    author=models.CharField(max_length=300)
    Blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    comment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author
    

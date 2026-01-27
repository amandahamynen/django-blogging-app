from django.shortcuts import render
from .models import BlogPost

def blogpost_list(request):
    blogposts = BlogPost.objects.all()
    return render(request, 'blogs/blogpost_list.html', {'blogposts': blogposts})

def blogpost_detail(request, blog_id):
    blogpost = BlogPost.objects.get(id=blog_id)
    return render(request, 'blogs/blogpost_detail.html', {'blogpost': blogpost})
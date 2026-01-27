from django.http import Http404
from django.shortcuts import render
from .models import BlogPost

def blogpost_list(request):
    blogposts = BlogPost.objects.all()
    return render(request, 'blogs/blogpost_list.html', {'blogposts': blogposts})

def blogpost_detail(request, blog_id):
    try:
        blogpost = BlogPost.objects.get(id=blog_id)
    except BlogPost.DoesNotExist:
        raise Http404("Blog post does not exist")
    return render(request, 'blogs/blogpost_detail.html', {'blogpost': blogpost})
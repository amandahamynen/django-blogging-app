from django.shortcuts import get_object_or_404, render
from .models import BlogPost

def blogpost_list(request):
    blogposts = BlogPost.objects.all()
    return render(request, 'blogs/blogpost_list.html', {'blogposts': blogposts})

def blogpost_detail(request, blogpost_id):
    blogpost = get_object_or_404(BlogPost, id=blogpost_id)
    return render(request, 'blogs/blogpost_detail.html', {'blogpost': blogpost})
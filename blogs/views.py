from django.shortcuts import get_object_or_404, redirect, render
from .models import BlogPost
from django.contrib.auth.decorators import login_required

@login_required(login_url='/users/login/')
def blogpost_list_all(request):
    blogposts = BlogPost.objects.all()
    return render(request, 'blogs/blogpost_list.html', {'blogposts': blogposts})

@login_required(login_url='/users/login/')
def blogpost_detail(request, blogpost_id):
    blogpost = get_object_or_404(BlogPost, id=blogpost_id)
    return render(request, 'blogs/blogpost_detail.html', {'blogpost': blogpost})

@login_required(login_url='/users/login/')
def blogpost_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        blogpost = BlogPost.objects.create(title=title, content=content, creator=request.user)
        return redirect('blogs:blogpost_detail', blogpost_id=blogpost.id)
    return render(request, 'blogs/blogpost_creation_form.html')
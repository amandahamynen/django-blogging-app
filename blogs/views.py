from django.shortcuts import get_object_or_404, redirect, render
from .models import BlogPost
from django.contrib.auth.decorators import login_required

@login_required(login_url='/users/login/')
def blogpost_list_all(request):
    blogposts = BlogPost.objects.filter(private=False)
    return render(request, 'blogs/blogpost_list.html', {'blogposts': blogposts})

@login_required(login_url='/users/login/')
def blogpost_list_my(request):
    blogposts = BlogPost.objects.filter(creator=request.user)
    return render(request, 'blogs/blogpost_list.html', {'blogposts': blogposts})

@login_required(login_url='/users/login/')
def blogpost_detail(request, blogpost_id):
    blogpost = get_object_or_404(BlogPost, id=blogpost_id)
    if request.method == 'POST':
        return redirect('blogs:blogpost_edit', blogpost_id=blogpost.id)
    return render(request, 'blogs/blogpost_detail.html', {'blogpost': blogpost})

@login_required(login_url='/users/login/')
def blogpost_edit(request, blogpost_id):
    blogpost = get_object_or_404(BlogPost, id=blogpost_id)
    if request.method == 'POST':
        blogpost.title = request.POST.get('title')
        blogpost.content = request.POST.get('content')
        blogpost.private = request.POST.get('private') == 'on'
        blogpost.save()
        return redirect('blogs:blogpost_detail', blogpost_id=blogpost.id)
    return render(request, 'blogs/blogpost_edit.html', {'blogpost': blogpost})

@login_required(login_url='/users/login/')
def blogpost_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        blogpost = BlogPost.objects.create(title=title, content=content, creator=request.user)
        return redirect('blogs:blogpost_detail', blogpost_id=blogpost.id)
    return render(request, 'blogs/blogpost_creation_form.html')
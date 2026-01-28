from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('blogs:blogpost_list')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html' , {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('blogs:blogpost_list')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

@login_required(login_url='/users/login/')
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return render(request, 'users/logout.html')
    return redirect('blogs:blogpost_list')
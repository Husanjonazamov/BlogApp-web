from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForms
from django.contrib.auth.views import LogoutView
from django.contrib.auth import logout
from .forms import UserUpdateForm, ProfileUpdateForm

def sign_up(requests):
    if requests.method == 'POST':
        form = SignUpForms(requests.POST)
        if form.is_valid():
            form.save()
            return redirect("users-login")
    else:
        form = SignUpForms()    
    context = {
        'form': form
    }
    return render(requests, "users/sign_up.html", context)


def logout_view(request):
    if request.method == 'POST':
        # Handle logout for POST request
        logout(request)
        return redirect('home')  # Redirect to the homepage or another URL
    elif request.method == 'GET':
        # Handle GET request appropriately (e.g., display a message or redirect)
        return redirect('LogoUT')  # Redirect to the login page

def LogoUt(request):
    return render(request, "users/logout.html")

def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST or None, instance = request.user)
        p_form = ProfileUpdateForm(request.POST or None, request.FILES or None, instance=request.user.profilemodel)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('users-profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profilemodel)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
        
    return render(request, "users/profile.html", context)
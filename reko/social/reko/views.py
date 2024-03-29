from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile

def home(request):
    return render(request, 'home.html', {})

def profile_list(request):
    if request.user.is_authenticated:
        profiles = Profile.objects.exclude(user=request.user)
        return render(request, 'profile_list.html', {"profiles": profiles})
    else:
        messages.success(request, ('You must log-in in order to view other profiles.'))
        return redirect('home')
    
def profile(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        return render(request, 'profile.html', {"profile": profile})
    else:
        messages.success(request, ('You must log-in in order to view other profiles.'))
        return redirect('home')
   
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, "main/home.html")

@login_required
def profile(request):
    return render(request, 'main/profile.html', {
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'email': request.user.email,
    })
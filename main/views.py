from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, "main/home.html")

@login_required
def profile(request):
    try:
        # Get user details
        name = request.user.get_full_name() or request.user.username
        email = request.user.email

        # Render the profile page
        return render(request, 'main/profile.html', {
            'name': name,
            'email': email,
        })
    except Exception as e:
        # Handle unexpected errors gracefully
        return render(request, 'main/error.html', {
            'error_message': 'An error occurred while loading your profile.',
            'details': str(e),
        })
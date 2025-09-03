# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import User
# from django.contrib import messages

# # Home view
# def home(request):
#     """Render the users home page."""
#     return render(request, 'users/home.html')


# # Signup view
# def signup_view(request):
#     """
#     Handles user signup:
#     - Checks password confirmation
#     - Checks duplicate username/email
#     - Creates new user
#     """
#     if request.method == "POST":
#         username = request.POST['username']
#         email = request.POST['email']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']

#         # Password confirmation check
#         if password1 != password2:
#             messages.error(request, "Passwords do not match")
#             return redirect('users:signup')

#         # Check if username already exists
#         if User.objects.filter(username=username).exists():
#             messages.error(request, "Username already taken")
#             return redirect('users:signup')

#         # Check if email already exists
#         if User.objects.filter(email=email).exists():
#             messages.error(request, "Email already used")
#             return redirect('users:signup')

#         # Create user
#         user = User.objects.create_user(username=username, email=email, password=password1)
#         user.save()
#         messages.success(request, "Account created successfully!")
#         return redirect('users:login')

#     return render(request, 'users/signup.html')


# # Login view
# def login_view(request):
#     """
#     Handles user login:
#     - Authenticates username/password
#     - Redirects to profile on success
#     """
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user:
#             login(request, user)
#             return redirect('users:profile')
#         else:
#             messages.error(request, "Invalid username or password")
#             return redirect('users:login')

#     return render(request, 'users/login.html')


# # Logout view
# def logout_view(request):
#     """Logs out the user and redirects to login page."""
#     logout(request)
#     return redirect('users:login')


# # Profile view
# def profile_view(request):
#     """Render the user profile page."""
#     return render(request, 'users/profile.html')


# from django.shortcuts import render
# from django.http import HttpResponse

# def signup_view(request):
#     return render(request, 'users/signup.html')

# def login_view(request):
#     return render(request, 'users/login.html')


# from django.shortcuts import render
# from django.http import HttpResponse

# def signup_view(request):
#     return render(request, 'users/signup.html')

# def login_view(request):
#     return render(request, 'users/login.html')











# from django.shortcuts import render

# # Homepage
# def home(request):
#     return render(request, 'users/home.html')

# # Signup page
# def signup_view(request):
#     return render(request, 'users/signup.html')

# # Login page
# def login_view(request):
#     return render(request, 'users/login.html')

# # Profile page
# def profile_view(request):
#     return render(request, 'users/profile.html')

from django.shortcuts import render, redirect
from django.contrib.auth import logout

# Homepage
# def home(request):
#     return render(request, 'users/home.html')

def home(request):
    return render(request, 'users/home.html')  # ya bas 'home.html' agar DIRS use ho raha

# Signup pages
def signup_view(request):
    return render(request, 'users/signup.html')

# Login page
def login_view(request):
    return render(request, 'users/login.html')

# Profile page
def profile_view(request):
    return render(request, 'users/profile.html')

# ✅ Logout view
def logout_view(request):
    logout(request)
    return redirect('users:login')










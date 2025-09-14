# app/users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

from app.users.services.user_service import create_user

User = get_user_model()

# ✅ Signup View
def signup_view(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        role = request.POST.get("role")

        # 🔒 Password Match Check
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, "users/signup.html")

        try:
            # ✅ Call Service Layer (role passed here)
            user = create_user(full_name, email, password, role)

            # ✅ Login user automatically after signup
            login(request, user)
            return redirect_user_based_on_role(user)

        except ValidationError as e:
            messages.error(request, str(e))
        except Exception:
            messages.error(request, "An unexpected error occurred.")
        
        return render(request, "users/signup.html")

    return render(request, "users/signup.html")


# ✅ Login View
def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, username=email, password=password)
        if user:
            login(request, user)
            return redirect_user_based_on_role(user)
        else:
            messages.error(request, "Invalid email or password.")
            
    return render(request, "users/login.html")


# ✅ Logout View
def logout_view(request):
    logout(request)
    return redirect("users:login")


# ✅ Role-based Redirect Function
def redirect_user_based_on_role(user):
    role_routes = {
        "student": "students:dashboard",
        "teacher": "teachers:dashboard",
        "admin": "admins:dashboard",
    }
    return redirect(reverse(role_routes.get(user.role, "home")))

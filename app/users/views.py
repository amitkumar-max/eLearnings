

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from config.constants import STUDENT_DASHBOARD, TEACHER_DASHBOARD, ADMIN_DASHBOARD
from .services.user_service import create_user
from app.courses.models import Course

User = get_user_model()

def home(request):
    courses = Course.objects.all()
    return render(request, "users/home.html", {"courses": courses})

def placeholder(request):
    return HttpResponse("This is a placeholder page. ✅")

def signup_view(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name", "").strip()
        email = request.POST.get("email", "").strip().lower()
        password = request.POST.get("password", "")
        confirm_password = request.POST.get("confirm_password", "")
        role = request.POST.get("role", "").strip().lower()

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, "users/signup.html", {"full_name": full_name, "email": email, "role": role})

        try:
            user = create_user(full_name=full_name, email=email, password=password, role=role)
            auth_user = authenticate(request, username=email, password=password)
            if auth_user:
                login(request, auth_user)
                return redirect_user_based_on_role(auth_user)
            messages.success(request, "Account created. Please log in.")
            return redirect("users:login")
        except ValidationError as e:
            messages.error(request, str(e))
        except Exception:
            messages.error(request, "An unexpected error occurred. Try again.")
        return render(request, "users/signup.html", {"full_name": full_name, "email": email, "role": role})

    return render(request, "users/signup.html")

def login_view(request):
    """
    Login view with 'next' support.
    """
    next_url = request.GET.get('next', request.POST.get('next', '/students/dashboard/'))

    if request.method == "POST":
        email = request.POST.get("email", "").strip().lower()
        password = request.POST.get("password", "")
        user = authenticate(request, username=email, password=password)
        if user:
            login(request, user)
            return redirect(next_url)
        messages.error(request, "Invalid email or password.")

    return render(request, "users/login.html", {"next": next_url})

def logout_view(request):
    logout(request)
    return redirect("users:login")

def redirect_user_based_on_role(user):
    if user.role == "student":
        return redirect(STUDENT_DASHBOARD)
    elif user.role == "teacher":
        return redirect(TEACHER_DASHBOARD)
    elif user.role == "admin":
        return redirect(ADMIN_DASHBOARD)
    return redirect("home")

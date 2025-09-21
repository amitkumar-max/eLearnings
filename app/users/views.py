

# users/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.http import HttpResponse

from .services.user_service import create_user
from config.constants import STUDENT_DASHBOARD, TEACHER_DASHBOARD, ADMIN_DASHBOARD
# from django.shortcuts import redirect
from app.courses.models import Course



User = get_user_model()



def home(request):
    courses = Course.objects.all()
    return render(request, "users/home.html", {"courses": courses})

# users/views.py

def placeholder(request):
    return HttpResponse("This is a placeholder page. ✅")

def signup_view(request):
    """
    Handles POST from the provided plain HTML form:
    fields: full_name, email, password, confirm_password, role
    """
    if request.method == "POST":
        full_name = request.POST.get("full_name", "").strip()
        email = request.POST.get("email", "").strip().lower()
        password = request.POST.get("password", "")
        confirm_password = request.POST.get("confirm_password", "")
        role = request.POST.get("role", "").strip().lower()

        # Basic checks
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, "users/signup.html", {
                "full_name": full_name,
                "email": email,
                "role": role
            })

        try:
            # Create user (service validates further)
            user = create_user(full_name=full_name, email=email, password=password, role=role)

            # Authenticate then login (so backend attribute is set)
            auth_user = authenticate(request, username=email, password=password)
            if auth_user is None:
                # Shouldn't normally happen, but fallback to asking user to login
                messages.success(request, "Account created. Please log in.")
                return redirect("users:login")

            login(request, auth_user)
            return redirect_user_based_on_role(auth_user)

        except ValidationError as e:
            messages.error(request, str(e))
        except Exception as e:
            # don't leak internal error, but log it in your real project
            messages.error(request, "An unexpected error occurred. Try again.")

        return render(request, "users/signup.html", {
            "full_name": full_name,
            "email": email,
            "role": role
        })

    # GET
    return render(request, "users/signup.html")

def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email", "").strip().lower()
        password = request.POST.get("password", "")
        user = authenticate(request, username=email, password=password)
        if user:
            login(request, user)
            return redirect_user_based_on_role(user)
        messages.error(request, "Invalid email or password.")
    return render(request, "users/login.html")

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


# # # from django.shortcuts import render, redirect
# # # from django.contrib.auth import authenticate, login, logout
# # # from django.contrib.auth.models import User
# # # from django.contrib import messages

# # # # Home view
# # # def home(request):
# # #     """Render the users home page."""
# # #     return render(request, 'users/home.html')


# # # # Signup view
# # # def signup_view(request):
# # #     """
# # #     Handles user signup:
# # #     - Checks password confirmation
# # #     - Checks duplicate username/email
# # #     - Creates new user
# # #     """
# # #     if request.method == "POST":
# # #         username = request.POST['username']
# # #         email = request.POST['email']
# # #         password1 = request.POST['password1']
# # #         password2 = request.POST['password2']

# # #         # Password confirmation check
# # #         if password1 != password2:
# # #             messages.error(request, "Passwords do not match")
# # #             return redirect('users:signup')

# # #         # Check if username already exists
# # #         if User.objects.filter(username=username).exists():
# # #             messages.error(request, "Username already taken")
# # #             return redirect('users:signup')

# # #         # Check if email already exists
# # #         if User.objects.filter(email=email).exists():
# # #             messages.error(request, "Email already used")
# # #             return redirect('users:signup')

# # #         # Create user
# # #         user = User.objects.create_user(username=username, email=email, password=password1)
# # #         user.save()
# # #         messages.success(request, "Account created successfully!")
# # #         return redirect('users:login')

# # #     return render(request, 'users/signup.html')


# # # # Login view
# # # def login_view(request):
# # #     """
# # #     Handles user login:
# # #     - Authenticates username/password
# # #     - Redirects to profile on success
# # #     """
# # #     if request.method == "POST":
# # #         username = request.POST['username']
# # #         password = request.POST['password']
# # #         user = authenticate(request, username=username, password=password)
# # #         if user:
# # #             login(request, user)
# # #             return redirect('users:profile')
# # #         else:
# # #             messages.error(request, "Invalid username or password")
# # #             return redirect('users:login')

# # #     return render(request, 'users/login.html')


# # # # Logout view
# # # def logout_view(request):
# # #     """Logs out the user and redirects to login page."""
# # #     logout(request)
# # #     return redirect('users:login')


# # # # Profile view
# # # def profile_view(request):
# # #     """Render the user profile page."""
# # #     return render(request, 'users/profile.html')


# # # from django.shortcuts import render
# # # from django.http import HttpResponse

# # # def signup_view(request):
# # #     return render(request, 'users/signup.html')

# # # def login_view(request):
# # #     return render(request, 'users/login.html')


# # # from django.shortcuts import render
# # # from django.http import HttpResponse

# # # def signup_view(request):
# # #     return render(request, 'users/signup.html')

# # # def login_view(request):
# # #     return render(request, 'users/login.html')











# # # from django.shortcuts import render

# # # # Homepage
# # # def home(request):
# # #     return render(request, 'users/home.html')

# # # # Signup page
# # # def signup_view(request):
# # #     return render(request, 'users/signup.html')

# # # # Login page
# # # def login_view(request):
# # #     return render(request, 'users/login.html')

# # # # Profile page
# # # def profile_view(request):
# # #     return render(request, 'users/profile.html')

# # from django.shortcuts import render, redirect
# # from django.contrib.auth import logout

# # # Homepage
# # # def home(request):
# # #     return render(request, 'users/home.html')

# # def home(request):
# #     return render(request, 'users/home.html')  # ya bas 'home.html' agar DIRS use ho raha

# # # Signup pages
# # def signup_view(request):
# #     return render(request, 'users/signup.html')

# # # Login page
# # def login_view(request):
# #     return render(request, 'users/login.html')

# # # Profile page
# # def profile_view(request):
# #     return render(request, 'users/profile.html')

# # # ✅ Logout view
# # def logout_view(request):
# #     logout(request)
# #     return redirect('users:login')







# from django.contrib.auth import login, logout, authenticate
# from django.shortcuts import render, redirect
# from django.views import View
# from .models import UserProfile

# class LoginView(View):
#     def get(self, request):
#         return render(request, 'users/login.html')

#     def post(self, request):
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user:
#             login(request, user)
#             return redirect('/')
#         return render(request, 'users/login.html', {'error': 'Invalid credentials'})

# class LogoutView(View):
#     def get(self, request):
#         logout(request)
#         return redirect('/')



# # app/users/views.py
# from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
# from django.contrib import messages
# from django.contrib.auth import authenticate, login, logout

# def signup_view(request):
#     if request.method == "POST":
#         full_name = request.POST.get("full_name")
#         email = request.POST.get("email")
#         password = request.POST.get("password")
#         confirm_password = request.POST.get("confirm_password")

#         if password != confirm_password:
#             messages.error(request, "Passwords do not match!")
#             return redirect("users:signup")

#         if User.objects.filter(username=email).exists():
#             messages.error(request, "User with this email already exists.")
#             return redirect("users:signup")

#         user = User.objects.create_user(
#             username=email,
#             email=email,
#             password=password,
#             first_name=full_name
#         )
#         messages.success(request, "Account created successfully! Please log in.")
#         return redirect("users:login")

#     return render(request, "users/signup.html")


# def login_view(request):
#     if request.method == "POST":
#         email = request.POST.get("email")
#         password = request.POST.get("password")
#         user = authenticate(request, username=email, password=password)

#         if user is not None:
#             login(request, user)
#             return redirect("home")
#         else:
#             messages.error(request, "Invalid email or password.")
#             return redirect("users:login")

#     return render(request, "users/login.html")


# def logout_view(request):
#     logout(request)
#     return redirect("users:login")





# from django.shortcuts import render, redirect
# from django.contrib.auth import login, authenticate, logout
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib import messages
# from .forms import CustomSignupForm
# from .models import User

# def signup_view(request):
#     if request.method == 'POST':
#         form = CustomSignupForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.username = user.email  # email as username
#             user.save()
#             login(request, user)
#             return redirect('users:role_redirect')
#         else:
#             messages.error(request, "Please correct the errors below.")
#     else:
#         form = CustomSignupForm()
#     return render(request, 'users/signup.html', {'form': form})

# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('users:role_redirect')
#         else:
#             messages.error(request, "Invalid credentials")
#     else:
#         form = AuthenticationForm()
#     return render(request, 'users/login.html', {'form': form})

# def logout_view(request):
#     logout(request)
#     return redirect('users:login')

# def role_redirect(request):
#     """Redirect users based on their role after login/signup"""
#     if not request.user.is_authenticated:
#         return redirect('users:login')

#     if request.user.role == "admin":
#         return redirect('admins:dashboard')
#     elif request.user.role == "teacher":
#         return redirect('teachers:dashboard')
#     else:
#         return redirect('students:dashboard')




# from django.shortcuts import render, redirect
# from django.contrib.auth import login, authenticate, logout
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib import messages
# from .forms import CustomSignupForm

# def signup_view(request):
#     if request.method == 'POST':
#         form = CustomSignupForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.username = user.email  # email as username
#             user.save()
#             login(request, user)
#             return redirect('users:role_redirect')
#         else:
#             messages.error(request, "Please correct the errors below.")
#     else:
#         form = CustomSignupForm()
#     return render(request, 'users/signup.html', {'form': form})

# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('users:role_redirect')
#         else:
#             messages.error(request, "Invalid credentials")
#     else:
#         form = AuthenticationForm()
#     return render(request, 'users/login.html', {'form': form})

# def logout_view(request):
#     logout(request)
#     return redirect('users:login')

# def role_redirect(request):
#     if not request.user.is_authenticated:
#         return redirect('users:login')

#     if request.user.role == "admin":
#         return redirect('admins:dashboard')
#     elif request.user.role == "teacher":
#         return redirect('teachers:dashboard')
#     return redirect('students:dashboard')




# app/users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

# ✅ Signup View
def signup_view(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        role = request.POST.get("role")

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, "signup.html")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered.")
            return render(request, "signup.html")

        user = User.objects.create_user(
            username=email,  # AbstractUser ke liye zaroori
            email=email,
            password=password,
            full_name=full_name,
            role=role
        )
        login(request, user)
        return redirect_user_based_on_role(user)

    return render(request, "signup.html")


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
            return render(request, "login.html")

    return render(request, "login.html")


# ✅ Logout View
def logout_view(request):
    logout(request)
    return redirect("users:login")


# ✅ Role-based Redirect Function
def redirect_user_based_on_role(user):
    if user.role == "student":
        return redirect(reverse("students:dashboard"))
    elif user.role == "teacher":
        return redirect(reverse("teachers:dashboard"))
    elif user.role == "admin":
        return redirect(reverse("admins:dashboard"))
    return redirect("/")  # fallback






















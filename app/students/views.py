from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# ---------- Dashboard ----------
@login_required
def dashboard(request):
    return render(request, "students/dashboard.html", {"user": request.user})

# ---------- Announcements ----------
def announcements(request):
    return render(request, "students/announcements.html")

def assignment_detail(request, id):
    return render(request, "students/assignments_details.html", {"id": id})

# ---------- Assignments ----------
def assignments(request):
    return render(request, "students/assignments.html")

# ---------- Courses ----------
def courses(request):
    return render(request, "students/courses.html")

def course_detail(request, id):
    return render(request, "students/courses_details.html", {"id": id})

def courses_list(request):
    return render(request, "students/courses_list.html")

# ---------- Discussions ----------
def discussions(request):
    return render(request, "students/discussions.html")

# ---------- My/Enrolled Courses ----------
def my_courses(request):
    return render(request, "students/my_courses.html")

def enrolled_courses(request):
    return render(request, "students/enrolled_courses.html")

# ---------- Grades ----------
def grades(request):
    return render(request, "students/grades.html")

# ---------- Login ----------
def login_view(request):
    return render(request, "students/login.html")

# ---------- Messages / Notifications ----------
def messages_view(request):
    return render(request, "students/messages.html")

def notifications(request):
    return render(request, "students/notifications.html")

# ---------- Progress / Settings ----------
def progress(request):
    return render(request, "students/progress.html")

def settings(request):
    return render(request, "students/settings.html")

# ---------- Profile ----------
def profile(request):
    return render(request, "students/profile.html")

def edit_profile(request):
    return render(request, "students/edit_profile.html")

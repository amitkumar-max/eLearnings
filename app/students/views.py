from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import StudentProfile, Enrollment, AssignmentSubmission
from app.courses.models import Course, Lesson, Exam

# ---------- Dashboard ----------
@login_required
def dashboard(request):
    # get_or_create ensures StudentProfile exists
    student, created = StudentProfile.objects.get_or_create(user=request.user)
    
    enrollments = Enrollment.objects.filter(student=student)
    
    total_courses = enrollments.count()
    overall_progress = sum([e.progress.get("completion_percentage", 0) for e in enrollments])
    overall_progress = overall_progress / total_courses if total_courses else 0

    context = {
        "student": student,
        "enrollments": enrollments,
        "overall_progress": overall_progress,
    }
    return render(request, "students/dashboard.html", context)


# ---------- Announcements ----------
def announcements(request):
    return render(request, "students/announcements.html")

# ---------- Assignments ----------
def assignments(request):
    student = StudentProfile.objects.get(user=request.user)
    submissions = AssignmentSubmission.objects.filter(student=student)
    return render(request, "students/assignments.html", {"submissions": submissions})

def assignment_detail(request, id):
    submission = AssignmentSubmission.objects.filter(id=id).first()
    return render(request, "students/assignments_details.html", {"submission": submission})

# ---------- Courses ----------
def courses(request):
    all_courses = Course.objects.all()
    return render(request, "students/courses.html", {"courses": all_courses})

def course_detail(request, id):
    course = Course.objects.filter(id=id).first()
    return render(request, "students/courses_details.html", {"course": course})

def courses_list(request):
    all_courses = Course.objects.all()
    return render(request, "students/courses_list.html", {"courses": all_courses})

# ---------- Discussions ----------
def discussions(request):
    return render(request, "students/discussions.html")

# ---------- My/Enrolled Courses ----------
def my_courses(request):
    student = StudentProfile.objects.get(user=request.user)
    enrollments = Enrollment.objects.filter(student=student)
    return render(request, "students/my_courses.html", {"enrollments": enrollments})

def enrolled_courses(request):
    student = StudentProfile.objects.get(user=request.user)
    enrollments = Enrollment.objects.filter(student=student)
    return render(request, "students/enrolled_courses.html", {"enrollments": enrollments})

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

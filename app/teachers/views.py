from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import TeacherProfile, TeacherAssignment, Schedule

@login_required
def dashboard(request):
    return render(request, "teachers/dashboard.html", {"user": request.user})

def announcements(request):
    return render(request, "teachers/announcements.html")

def announcement_detail(request, id):
    return render(request, "teachers/announcements_details.html", {"id": id})

def courses(request):
    return render(request, "teachers/courses.html")

def course_detail(request, id):
    return render(request, "teachers/course_details.html", {"id": id})

def assignments(request):
    # Show only assignments for logged-in teacher
    assignments = TeacherAssignment.objects.filter(teacher__user=request.user)
    return render(request, "teachers/assignments.html", {"assignments": assignments})

def assignment_detail(request, id):
    assignment = get_object_or_404(TeacherAssignment, id=id, teacher__user=request.user)
    return render(request, "teachers/assignments_details.html", {"assignment": assignment})

def schedule(request):
    schedule = Schedule.objects.filter(teacher__user=request.user)
    return render(request, "teachers/schedule.html", {"schedule": schedule})

def create_course(request):
    return render(request, "teachers/create_course.html")

def edit_course(request, id):
    return render(request, "teachers/edit_course.html", {"id": id})

def my_courses(request):
    return render(request, "teachers/my_courses.html")

def grade_submission(request):
    return render(request, "teachers/grade_submission.html")

def manage_students(request):
    return render(request, "teachers/manage_students.html")

def profile(request):
    return render(request, "teachers/profile.html")

def edit_profile(request):
    return render(request, "teachers/edit_profile.html")

def messages_view(request):
    return render(request, "teachers/messages.html")



def notifications(request):
    return render(request, "teachers/notifications.html")

def reports(request):
    return render(request, "teachers/reports.html")

def settings(request):
    return render(request, "teachers/settings.html")

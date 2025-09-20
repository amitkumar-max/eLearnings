from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    # yahan teacher specific data fetch kar sakte ho
    return render(request, "teachers/dashboard.html", {"user": request.user})

def announcements(request):
    return render(request, "teachers/announcements.html")

def assignment_detail(request, id):
    return render(request, "teachers/assignments_details.html", {"id": id})


def announcement_detail(request, id):
    return render(request, "teachers/announcements_details.html", {"id": id})

def courses(request):
    return render(request, "teachers/courses.html")

def course_detail(request, id):
    return render(request, "teachers/course_details.html", {"id": id})

def assignments(request):
    return render(request, "teachers/assignments.html")

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

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import StudentProfile, Enrollment, AssignmentSubmission
from app.courses.models import Course, Lesson, Exam


from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from app.students.models import StudentProfile, Enrollment
from app.courses.models import Course
from app.notifications.models import Notification
from django.http import JsonResponse


@login_required
def fetch_notifications(request):
    # fetch unread notifications for current user
    notifications = Notification.objects.filter(user=request.user, is_read=False).order_by('-created_at')
    data = []
    for n in notifications:
        data.append({
            "id": n.id,
            "title": n.title,
            "message": n.message,
            "type": n.notification_type,
            "created_at": n.created_at.strftime("%Y-%m-%d %H:%M:%S")
        })
    return JsonResponse({"notifications": data})



@login_required
def enroll_course(request, course_id):
    student_profile = StudentProfile.objects.get(user=request.user)
    course = get_object_or_404(Course, id=course_id)

    enrollment, created = Enrollment.objects.get_or_create(
        student=student_profile, course=course
    )

    if created:
        # Notification creation
        Notification.objects.create(
            user=request.user,
            course=course,
            title="Enrollment Successful",
            message=f"You have successfully enrolled in {course.title}!",
            notification_type="SUCCESS"
        )

    return redirect("students:dashboard")


@login_required
def student_notifications(request):
    notifications = request.user.notifications.all()
    return render(request, "students/notifications.html", {"notifications": notifications})

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

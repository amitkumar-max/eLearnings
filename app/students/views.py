from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth import logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

from app.students.models import StudentProfile, Enrollment, AssignmentSubmission
from app.courses.models import Course, Lesson, Exam, CourseAssignment
from app.notifications.models import Notification

# ---------------- Dashboard ----------------
@login_required
def dashboard(request):
    student, _ = StudentProfile.objects.get_or_create(user=request.user)
    enrollments = Enrollment.objects.filter(student=student)
    courses = [enroll.course for enroll in enrollments]

    context = {
        "student": student,
        "total_courses": len(courses),
        "completed_lessons": student.completed_lessons.count(),
        "pending_assignments": student.pending_assignments.count(),
        "overall_progress": student.progress_percentage(),
        "courses": courses,
    }
    return render(request, "students/dashboard.html", context)

# ---------------- Courses ----------------
@login_required
def courses(request):
    all_courses = Course.objects.all()
    return render(request, "students/courses.html", {"courses": all_courses})

@login_required
def course_detail(request, id):
    course = get_object_or_404(Course, id=id)
    return render(request, "students/courses_details.html", {"course": course})

@login_required
def courses_list(request):
    all_courses = Course.objects.all()
    return render(request, "students/courses_list.html", {"courses": all_courses})

@login_required
def my_courses(request):
    student, _ = StudentProfile.objects.get_or_create(user=request.user)
    enrollments = Enrollment.objects.filter(student=student)
    courses = [enroll.course for enroll in enrollments]

    return render(request, "students/my_courses.html", {
        "student": student,
        "enrollments": enrollments,
        "courses": courses,
    })

@login_required
def enrolled_courses(request):
    student = StudentProfile.objects.get(user=request.user)
    enrollments = Enrollment.objects.filter(student=student)
    return render(request, "students/enrolled_courses.html", {"enrollments": enrollments})

# ---------------- Enrollment ----------------
# @login_required
# def enroll_course(request, course_id):
#     student, _ = StudentProfile.objects.get_or_create(user=request.user)
#     course = get_object_or_404(Course, id=course_id)

#     enrollment, created = Enrollment.objects.get_or_create(student=student, course=course)
#     if created:
#         Notification.objects.create(
#             user=request.user,
#             course=course,
#             title="Enrollment Successful",
#             message=f"You have successfully enrolled in {course.title}!",
#             notification_type="SUCCESS"
#         )
#         messages.success(request, f"You are now enrolled in {course.title}.")
#     else:
#         messages.info(request, f"You are already enrolled in {course.title}.")

#     return redirect("students:dashboard")

# views.py

@login_required
def enroll_course(request, course_id):
    student, _ = StudentProfile.objects.get_or_create(user=request.user)
    course = get_object_or_404(Course, id=course_id)

    enrollment, created = Enrollment.objects.get_or_create(student=student, course=course)

    if created:
        # Notification create
        Notification.objects.create(
            user=request.user,
            course=course,
            title="Enrollment Successful",
            message=f"You have successfully enrolled in {course.title}!",
            notification_type="SUCCESS"
        )
        messages.success(request, f"You are now enrolled in {course.title}.")
    else:
        messages.info(request, f"You are already enrolled in {course.title}.")

    # Redirect back to the course detail page instead of dashboard
    return redirect('course_detail', id=course.id)




# ---------------- Assignments ----------------
@login_required
def assignments(request):
    student = StudentProfile.objects.get(user=request.user)
    submissions = AssignmentSubmission.objects.filter(student=student)
    return render(request, "students/assignments.html", {"submissions": submissions})

@login_required
def assignment_detail(request, id):
    submission = get_object_or_404(AssignmentSubmission, id=id)
    return render(request, "students/assignments_details.html", {"submission": submission})

# ---------------- Notifications ----------------
@login_required
def fetch_notifications(request):
    notifications = Notification.objects.filter(user=request.user, is_read=False).order_by('-created_at')
    data = []

    if notifications.exists():
        for n in notifications:
            data.append({
                "id": n.id,
                "title": n.title,
                "message": n.message,
                "type": n.notification_type,
                "created_at": n.created_at.strftime("%Y-%m-%d %H:%M:%S")
            })
        notifications.update(is_read=True)
    else:
        data = [
            {"title": "Welcome!", "message": "You logged in successfully", "type": "info"},
            {"title": "Course Update", "message": "New assignment uploaded", "type": "success"},
        ]
    return JsonResponse({"notifications": data})

@login_required
def student_notifications(request):
    notifications = request.user.notifications.all()
    return render(request, "students/notifications.html", {"notifications": notifications})

# ---------------- Misc Views ----------------
@login_required
def grades(request): return render(request, "students/grades.html")
@login_required
def login_view(request): return render(request, "students/login.html")
@login_required
def messages_view(request): return render(request, "students/messages.html")
@login_required
def progress(request): return render(request, "students/progress.html")
@login_required
def settings(request): return render(request, "students/settings.html")
@login_required
def profile(request): return render(request, "students/profile.html")
@login_required
def edit_profile(request): return render(request, "students/edit_profile.html")
@login_required
def discussions(request): return render(request, "students/discussions.html")
@login_required
def announcements(request): return render(request, "students/announcements.html")
@login_required
def logout_view(request):
    logout(request)
    return redirect('students:login')
@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Password changed successfully.")
            return redirect('students:settings')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'students/change_password.html', {'form': form})

@login_required
def start_course(request, slug):
    course = get_object_or_404(Course, slug=slug)
    return render(request, "courses/start_course.html", {"course": course})

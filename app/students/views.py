from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth import logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
# Models
from app.students.models import StudentProfile, Enrollment, AssignmentSubmission
from app.courses.models import Course, Lesson, Exam, CourseAssignment
from app.notifications.models import Notification
from django.contrib import messages


@login_required
def start_course(request, slug):
    course = get_object_or_404(Course, slug=slug)
    return render(request, "courses/start_course.html", {"course": course})

@login_required
def my_courses(request):
    from django.contrib import messages  # make sure this import is at top

    # Safely get or create the student profile
    student, created = StudentProfile.objects.get_or_create(user=request.user)

    if created:
        messages.info(request, "Your student profile has been created automatically.")

    # Query enrolled courses safely
    enrollments = Enrollment.objects.filter(student=student)
    courses = [enrollment.course for enrollment in enrollments]

    return render(request, "students/my_courses.html", {
        "student": student,
        "enrollments": enrollments,
        "courses": courses,
    })

    
    
# ---------- Notifications ----------
@login_required
def fetch_notifications(request):
    # Fetch unread notifications from DB
    notifications = Notification.objects.filter(
        user=request.user, is_read=False
    ).order_by('-created_at')

    if notifications.exists():
        # If DB has notifications
        data = [
            {
                "id": n.id,
                "title": n.title,
                "message": n.message,
                "type": n.notification_type,
                "created_at": n.created_at.strftime("%Y-%m-%d %H:%M:%S")
            }
            for n in notifications
        ]

        # ✅ Mark them as read (so they don’t show again next fetch)
        notifications.update(is_read=True)

    else:
        # OR → fallback to dummy notifications
        data = [
            {"title": "Welcome!", "message": "You logged in successfully", "type": "info"},
            {"title": "Course Update", "message": "New assignment uploaded", "type": "success"},
        ]

    return JsonResponse({"notifications": data})
@login_required
def student_notifications(request):
    notifications = request.user.notifications.all()
    return render(request, "students/notifications.html", {"notifications": notifications})
# ---------- Dashboard ----------
@login_required
def dashboard(request):
    student, _ = StudentProfile.objects.get_or_create(user=request.user)
    context = {
        "student": student,
        "total_courses": student.enrolled_courses.count(),
        "completed_lessons": student.completed_lessons.count(),
        "pending_assignments": student.pending_assignments.count(),
        "overall_progress": student.progress_percentage(),
        "courses": courses,   # ✅ added this line
        
    }
    return render(request, "students/dashboard.html", context)
# ---------- Enroll Course ----------
@login_required
def enroll_course(request, course_id):
    student = StudentProfile.objects.get(user=request.user)
    course = get_object_or_404(Course, id=course_id)

    enrollment, created = Enrollment.objects.get_or_create(student=student, course=course)

    if created:
        Notification.objects.create(
            user=request.user,
            course=course,
            title="Enrollment Successful",
            message=f"You have successfully enrolled in {course.title}!",
            notification_type="SUCCESS"
        )

    return redirect("students:dashboard")
# ---------- Assignments ----------
@login_required
def assignments(request):
    student = StudentProfile.objects.get(user=request.user)
    submissions = AssignmentSubmission.objects.filter(student=student)
    return render(request, "students/assignments.html", {"submissions": submissions})
@login_required
def assignment_detail(request, id):
    submission = AssignmentSubmission.objects.filter(id=id).first()
    return render(request, "students/assignments_details.html", {"submission": submission})
# ---------- Courses ----------
@login_required
def courses(request):
    all_courses = Course.objects.all()
    return render(request, "students/courses.html", {"courses": all_courses})
@login_required
def course_detail(request, id):
    course = Course.objects.filter(id=id).first()
    return render(request, "students/courses_details.html", {"course": course})
@login_required
def courses_list(request):
    all_courses = Course.objects.all()
    return render(request, "students/courses_list.html", {"courses": all_courses})
@login_required
def my_courses(request):
    student = StudentProfile.objects.get(user=request.user)
    enrollments = Enrollment.objects.filter(student=student)
    return render(request, "students/my_courses.html", {"enrollments": enrollments})
@login_required
def enrolled_courses(request):
    student = StudentProfile.objects.get(user=request.user)
    enrollments = Enrollment.objects.filter(student=student)
    return render(request, "students/enrolled_courses.html", {"enrollments": enrollments})
# ---------- Misc Views ----------
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
    logout(request)  # logs out the user
    return redirect('students:login')  # redirect to login page after logout
@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # keep user logged in
            return redirect('students:settings')  # redirect after password change
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'students/change_password.html', {'form': form})




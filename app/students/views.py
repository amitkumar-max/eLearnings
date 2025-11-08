from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth import logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

from app.students.models import StudentProfile, Enrollment, AssignmentSubmission
from app.courses.models import Course, Lesson
from app.notifications.models import Notification


# ---------------- Dashboard ----------------
@login_required
def dashboard(request):
    student, _ = StudentProfile.objects.get_or_create(user=request.user)
    enrollments = Enrollment.objects.filter(student=student).select_related("course")
    courses = [e.course for e in enrollments]
    notifications = student.notifications.order_by('-created_at')[:10]

    context = {
        "student": student,
        "total_courses": len(courses),
        "completed_lessons": student.completed_lessons.count(),
        "pending_assignments": student.pending_assignments.count(),
        "overall_progress": student.progress_percentage(),
        "courses": courses,
        "notifications": notifications,
    }
    return render(request, "students/dashboard.html", context)


# ---------------- Enrollment Logic ----------------
@login_required
def enroll_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    student, _ = StudentProfile.objects.get_or_create(user=request.user)

    enrollment, created = Enrollment.objects.get_or_create(student=student, course=course)

    if created:
        Notification.objects.create(
            student=student,
            message=f"You have successfully enrolled in {course.title}!"
        )
        messages.success(request, f"Enrolled in {course.title} successfully!")
    else:
        messages.info(request, f"Already enrolled in {course.title}.")

    return redirect('students:course_detail', course_id=course.id)


# ---------------- Course Detail ----------------
@login_required
def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, "students/course_detail.html", {"course": course})


# ---------------- Course Listings ----------------
@login_required
def courses_list(request):
    return render(request, "students/courses_list.html", {"courses": Course.objects.all()})


@login_required
def my_courses(request):
    student, _ = StudentProfile.objects.get_or_create(user=request.user)
    enrollments = Enrollment.objects.filter(student=student).select_related("course")
    return render(request, "students/my_courses.html", {
        "student": student,
        "enrollments": enrollments,
        "courses": [e.course for e in enrollments],
    })


# ---------------- Assignments ----------------
@login_required
def assignments(request):
    student = StudentProfile.objects.get(user=request.user)
    submissions = AssignmentSubmission.objects.filter(student=student)
    return render(request, "students/assignments.html", {"submissions": submissions})


@login_required
def assignment_detail(request, id):
    submission = get_object_or_404(AssignmentSubmission, id=id)
    return render(request, "students/assignment_details.html", {"submission": submission})


# ---------------- Notifications ----------------
@login_required
def fetch_notifications(request):
    student = StudentProfile.objects.get(user=request.user)
    notifications = student.notifications.order_by('-created_at')

    if notifications.exists():
        data = [
            {
                "id": n.id,
                "message": n.message,
                "created_at": n.created_at.strftime("%Y-%m-%d %H:%M:%S")
            }
            for n in notifications
        ]
        notifications.update(is_read=True)
    else:
        data = [{"message": "No new notifications available.", "created_at": ""}]

    return JsonResponse({"notifications": data})


@login_required
def student_notifications(request):
    student = StudentProfile.objects.get(user=request.user)
    return render(request, "students/notifications.html", {"notifications": student.notifications.all()})


# ---------------- Miscellaneous Views ----------------
@login_required
def grades(request):
    return render(request, "students/grades.html")

@login_required
def messages_view(request):
    return render(request, "students/messages.html")

@login_required
def progress(request):
    return render(request, "students/progress.html")

@login_required
def settings(request):
    return render(request, "students/settings.html")

@login_required
def profile(request):
    return render(request, "students/profile.html")

@login_required
def edit_profile(request):
    return render(request, "students/edit_profile.html")

@login_required
def discussions(request):
    return render(request, "students/discussions.html")

@login_required
def announcements(request):
    return render(request, "students/announcements.html")


# ---------------- Auth Utilities ----------------
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def change_password(request):
    form = PasswordChangeForm(request.user, request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        update_session_auth_hash(request, user)
        messages.success(request, "Password changed successfully.")
        return redirect('students:settings')
    return render(request, 'students/change_password.html', {'form': form})


# ---------------- Course Start ----------------
@login_required
def start_course(request, slug):
    course = get_object_or_404(Course, slug=slug)
    lessons = Lesson.objects.filter(course=course).order_by('id')
    return render(request, 'students/start_course.html', {
        'course': course,
        'lessons': lessons,
    })

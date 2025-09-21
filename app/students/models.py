from django.db import models
from django.conf import settings

# ---------- Student Profile ----------
class StudentProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    wishlist_courses = models.ManyToManyField(
        "courses.Course",
        related_name="wishlisted_by",
        blank=True
    )
    progress = models.JSONField(default=dict)        # {course_id: completion_percentage}
    exam_scores = models.JSONField(default=dict)     # {exam_id: score}
    assignments_submitted = models.JSONField(default=dict)  # {lesson_id: status}
    last_login_ip = models.GenericIPAddressField(blank=True, null=True)
    points = models.IntegerField(default=0)
    achievements = models.JSONField(default=list)    # badges, trophies, etc.

    def __str__(self):
        return self.user.username

# ---------- Enrollment ----------
class Enrollment(models.Model):
    student = models.ForeignKey(
        "students.StudentProfile",
        on_delete=models.CASCADE,
        related_name="enrollments"
    )
    course = models.ForeignKey(
        "courses.Course",
        on_delete=models.CASCADE,
        related_name="enrolled_students"
    )
    date_enrolled = models.DateTimeField(auto_now_add=True)
    progress = models.JSONField(default=dict)  # {lesson_id: completion_percentage}

    def __str__(self):
        return f"{self.student.user.username} -> {self.course.title}"

# ---------- Assignment Submission ----------
class AssignmentSubmission(models.Model):
    student = models.ForeignKey(
        "students.StudentProfile",
        on_delete=models.CASCADE,
        related_name="assignment_submissions"
    )
    lesson = models.ForeignKey(
        "courses.Lesson",
        on_delete=models.CASCADE,
        related_name="submissions"
    )
    submitted_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default="submitted")  # submitted, pending, graded
    marks_obtained = models.IntegerField(default=0)
    feedback = models.TextField(blank=True)

    def __str__(self):
        return f"{self.student.user.username} -> {self.lesson.title}"

from django.db import models
from django.conf import settings

class StudentProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    wishlist_courses = models.ManyToManyField(
        "courses.Course",
        related_name="wishlisted_by",
        blank=True
    )
    bio = models.TextField(blank=True, null=True)
    progress = models.JSONField(default=dict)
    exam_scores = models.JSONField(default=dict)
    assignments_submitted = models.JSONField(default=dict)
    last_login_ip = models.GenericIPAddressField(blank=True, null=True)
    points = models.IntegerField(default=0)
    achievements = models.JSONField(default=list)

    # Dynamic dashboard fields
    enrolled_courses = models.ManyToManyField(
        "courses.Course",
        related_name='students',
        blank=True
    )
    completed_lessons = models.ManyToManyField(
        "courses.Lesson",
        blank=True
    )
    pending_assignments = models.ManyToManyField(
        'courses.CourseAssignment',
        related_name="pending_students"
    )

    def progress_percentage(self):
        total_lessons = sum(course.lessons.count() for course in self.enrolled_courses.all())
        if total_lessons == 0:
            return 0
        return int((self.completed_lessons.count() / total_lessons) * 100)

    def __str__(self):
        return self.user.email

class Enrollment(models.Model):
    student = models.ForeignKey(
        "students.StudentProfile",
        on_delete=models.CASCADE,
        related_name="enrollment_records"
    )
    course = models.ForeignKey(
        "courses.Course",
        on_delete=models.CASCADE,
        related_name="enrollment_records"
    )
    date_enrolled = models.DateTimeField(auto_now_add=True)
    progress = models.JSONField(default=dict)

    def __str__(self):
        return f"{self.student.user.email} -> {self.course.title}"

class ExamProgress(models.Model):
    student = models.ForeignKey(
        "students.StudentProfile",
        on_delete=models.CASCADE,
        related_name="exam_progress_records",
        null=True
    )
    exam = models.ForeignKey(
        "courses.Exam",
        on_delete=models.CASCADE,
        related_name="students_progress",
        null=True
    )
    completed = models.BooleanField(default=False)
    score = models.DecimalField(max_digits=6, decimal_places=2, default=0)

class AssignmentSubmission(models.Model):
    student = models.ForeignKey(
        "students.StudentProfile",
        on_delete=models.CASCADE,
        related_name="assignment_submissions"
    )
    exam = models.ForeignKey(
    "courses.Exam",
    on_delete=models.CASCADE,
    related_name="submitted_assignments",  # unique name
    null=True
    )
    submitted_at = models.DateTimeField(auto_now_add=True)
    score = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=20, default="pending")

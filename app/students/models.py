# students/models.py
from django.db import models
from django.conf import settings
from app.courses.models import Course

class StudentProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    wishlist_courses = models.ManyToManyField(Course, related_name="wishlisted_by", blank=True)
    progress = models.JSONField(default=dict)
    exam_scores = models.JSONField(default=dict)
    assignments_submitted = models.JSONField(default=dict)
    last_login_ip = models.GenericIPAddressField(blank=True, null=True)
    points = models.IntegerField(default=0)
    achievements = models.JSONField(default=list)

    def __str__(self):
        return self.user.email

class Enrollment(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateTimeField(auto_now_add=True)
    progress = models.JSONField(default=dict)

    def __str__(self):
        return f"{self.student.user.email} -> {self.course.title}"

class ExamProgress(models.Model):
    student = models.ForeignKey(
        StudentProfile, 
        on_delete=models.CASCADE, 
        related_name="exam_progress_records",
        null=True,       # temporary
    )
    exam = models.ForeignKey(
        'exams.Exam',  
        on_delete=models.CASCADE,
        related_name="students_progress",
        null=True,       # temporary
    )
    completed = models.BooleanField(default=False)
    score = models.DecimalField(max_digits=6, decimal_places=2, default=0)
class AssignmentSubmission(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    exam = models.ForeignKey(
        'exams.Exam',
        on_delete=models.CASCADE,
        related_name="assignment_submissions",
        null=True  # <-- ye line temporary null allow ke liye
    )
    submitted_at = models.DateTimeField(auto_now_add=True)
    score = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=20, default="pending")

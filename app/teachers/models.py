from django.db import models
from django.conf import settings
from ..courses.models import Course

# Teacher Profile
class TeacherProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    courses_created = models.ManyToManyField(Course, blank=True)
    bio = models.TextField(blank=True, null=True)
    statistics = models.JSONField(default=dict)  # student_feedback, ratings, earnings
    awards = models.JSONField(default=list)  # achievements, certifications
    profile_views = models.IntegerField(default=0)
    social_links = models.JSONField(default=dict)  # {"linkedin": "", "twitter": ""}

    def __str__(self):
        return self.user.username


# Assignments
class Assignment(models.Model):
    teacher = models.ForeignKey(TeacherProfile, on_delete=models.CASCADE, related_name="assignments")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="assignments")
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.course.name})"


# Schedule / Timetable
class Schedule(models.Model):
    teacher = models.ForeignKey(TeacherProfile, on_delete=models.CASCADE, related_name="schedules")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="schedules")
    date = models.DateField()
    time = models.TimeField()
    topic = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.course.name} - {self.date} {self.time}"




from django.utils import timezone

from django.db import models
from django.conf import settings

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class TeacherProfile(TimeStampedModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    courses_created = models.ManyToManyField('courses.Course', blank=True,  related_name="creators")
    bio = models.TextField(blank=True, null=True)
    statistics = models.JSONField(default=dict)
    awards = models.JSONField(default=list)
    profile_views = models.IntegerField(default=0)
    social_links = models.JSONField(default=dict)

    def __str__(self):
        return self.user.full_name

class TeacherAssignment(TimeStampedModel):
    teacher = models.ForeignKey(
        'teachers.TeacherProfile',
        on_delete=models.CASCADE,
        related_name="assignments_by_teacher"
    )
    course = models.ForeignKey(
        'courses.Course',
        on_delete=models.CASCADE,
        related_name="assignments_in_course"
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.title} ({self.course.title})"

class Schedule(TimeStampedModel):
    teacher = models.ForeignKey(
        'teachers.TeacherProfile',
        on_delete=models.CASCADE,
        related_name="schedules"
    )
    course = models.ForeignKey(
        'courses.Course',
        on_delete=models.CASCADE,
        related_name="course_schedules"
    )
    date = models.DateField(default=timezone.now)
    time = models.TimeField(null=True, blank=True)
    topic = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.course.title} - {self.date} {self.time}"

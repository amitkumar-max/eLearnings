from django.db import models
from django.conf import settings

class TeacherProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    courses_created = models.ManyToManyField("courses.Course", blank=True)
    bio = models.TextField(blank=True, null=True)
    statistics = models.JSONField(default=dict)  # student_feedback, ratings, earnings
    awards = models.JSONField(default=list)  # achievements, certifications
    profile_views = models.IntegerField(default=0)
    social_links = models.JSONField(default=dict)  # {"linkedin": "", "twitter": ""}

    def __str__(self):
        return self.user.username

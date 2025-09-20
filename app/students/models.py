from django.db import models
from django.conf import settings

class StudentProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    courses_purchased = models.ManyToManyField("courses.Course", blank=True)
    progress = models.JSONField(default=dict)  # {course_id: completion_percentage}
    statistics = models.JSONField(default=dict)  # quiz_scores, attempts, streaks
    last_login_ip = models.GenericIPAddressField(blank=True, null=True)
    points = models.IntegerField(default=0)
    achievements = models.JSONField(default=list)  # badges, trophies, etc.
    wishlist_courses = models.ManyToManyField("courses.Course", related_name="wishlisted_by", blank=True)

    def __str__(self):
        return self.user.username

from django.db import models
from django.conf import settings

class AdminProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    permissions_notes = models.TextField(blank=True, null=True)
    managed_sections = models.JSONField(default=list)  # e.g., ["users", "courses"]
    last_login_ip = models.GenericIPAddressField(blank=True, null=True)
    super_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username





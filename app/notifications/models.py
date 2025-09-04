# app/notifications/models.py
from django.db import models
from django.conf import settings

class Notification(models.Model):
    NOTIFICATION_TYPES = [
        ('INFO', 'Information'),
        ('SUCCESS', 'Success'),
        ('WARNING', 'Warning'),
        ('ERROR', 'Error'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications')
    title = models.CharField(max_length=255)
    message = models.TextField()
    notification_type = models.CharField(max_length=10, choices=NOTIFICATION_TYPES, default='INFO')
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.title}"

    class Meta:
        ordering = ['-created_at']

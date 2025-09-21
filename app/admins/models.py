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


# Optional: Track courses if admin wants to approve/manage courses
class ManagedCourse(models.Model):
    admin = models.ForeignKey(AdminProfile, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.course_name} - {self.admin.user.username}"


# Optional: Track payments handled by admin
class AdminPaymentLog(models.Model):
    admin = models.ForeignKey(AdminProfile, on_delete=models.CASCADE)
    amount = models.FloatField()
    student_name = models.CharField(max_length=255)
    course_name = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default="completed")  # pending, completed, failed

    def __str__(self):
        return f"{self.course_name} - {self.amount} by {self.admin.user.username}"


# Optional: Notifications created by admin
class AdminNotification(models.Model):
    admin = models.ForeignKey(AdminProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} - {self.admin.user.username}"


# Optional: Support tickets handled by admin
class SupportTicket(models.Model):
    admin = models.ForeignKey(AdminProfile, on_delete=models.SET_NULL, null=True, blank=True)
    student_name = models.CharField(max_length=255)
    message = models.TextField()
    resolved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ticket from {self.student_name} - {'Resolved' if self.resolved else 'Pending'}"

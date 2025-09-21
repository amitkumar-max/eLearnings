from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Enrollment
from app.notifications.models import Notification

@receiver(post_save, sender=Enrollment)
def send_enrollment_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            user=instance.student.user,
            course=instance.course,
            title="Enrollment Successful",
            message=f"You have successfully enrolled in {instance.course.title}!",
            notification_type="SUCCESS"
        )

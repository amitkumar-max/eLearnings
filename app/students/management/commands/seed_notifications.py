from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from app.notifications.models import Notification  # adjust import if needed

User = get_user_model()

class Command(BaseCommand):
    help = "Seed test notifications for a user"

    def handle(self, *args, **kwargs):
        try:
            user = User.objects.first()  # get first user for demo
            if not user:
                self.stdout.write(self.style.ERROR("No users found!"))
                return

            Notification.objects.create(
                user=user,
                title="Assignment Due",
                message="Your assignment for Math is due tomorrow!",
                notification_type="warning"
            )
            Notification.objects.create(
                user=user,
                title="New Exam",
                message="A new exam has been scheduled next week.",
                notification_type="info"
            )

            self.stdout.write(self.style.SUCCESS("Dummy notifications created ✅"))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error: {e}"))

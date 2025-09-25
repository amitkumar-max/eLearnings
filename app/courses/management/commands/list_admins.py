from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = 'List all admin/superuser accounts'

    def handle(self, *args, **kwargs):
        admins = User.objects.filter(is_superuser=True)
        if not admins.exists():
            self.stdout.write("No admin users found.")
            return

        self.stdout.write("Admin Users:")
        for admin in admins:
            self.stdout.write(f"- Username: {admin.username}, Email: {admin.email}")

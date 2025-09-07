# # from django.db import models
# # from django.contrib.auth.models import User

# # # Optional: extra profile fields
# # class Profile(models.Model):
# #     user = models.OneToOneField(User, on_delete=models.CASCADE)
# #     bio = models.TextField(blank=True, null=True)
# #     avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

# #     def __str__(self):
# #         return self.user.username




# # from django.db import models
# # from django.contrib.auth.models import AbstractUser

# # # Example: custom user model (optional)
# # class CustomUser(AbstractUser):
# #     pass


# from django.db import models
# from django.contrib.auth.models import User

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     bio = models.TextField(blank=True, null=True)
#     avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

#     def __str__(self):
#         return self.user.username

# from django.db import models
# from django.conf import settings
# from courses.models import Course, TimeStampedModel

# class UserProfile(TimeStampedModel):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile")
#     bio = models.CharField(max_length=280, blank=True)
#     avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)
#     phone = models.CharField(max_length=20, blank=True)
#     country = models.CharField(max_length=60, blank=True)
#     preferences = models.JSONField(default=dict, blank=True)
#     enrolled_courses = models.ManyToManyField(Course, blank=True, related_name="enrolled_users")

#     def __str__(self):
#         return f"Profile: {self.user.username}"





# from django.contrib.auth.models import AbstractUser
# from django.db import models

# class User(AbstractUser):
#     ROLES = (
#         ('student', 'Student'),
#         ('teacher', 'Teacher'),
#         ('admin', 'Admin'),
#     )
#     full_name = models.CharField(max_length=150)
#     email = models.EmailField(unique=True)
#     role = models.CharField(max_length=10, choices=ROLES, default='student')

#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = ["username"]

#     def __str__(self):
#         return f"{self.full_name} ({self.role})"




# app/users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('admin', 'Admin'),
    ]
    full_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "full_name"]

    def __str__(self):
        return f"{self.full_name} ({self.role})"

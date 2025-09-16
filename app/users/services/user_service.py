# users/services/user_service.py
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()

VALID_ROLES = {"student", "teacher", "admin"}

def create_user(full_name: str, email: str, password: str, role: str = "student"):
    """
    Creates a user after basic validation.
    Raises ValidationError on failure.
    """
    email = (email or "").strip().lower()
    role = (role or "student").strip().lower()

    if not email:
        raise ValidationError("Email is required.")
    if not password or len(password) < 6:
        raise ValidationError("Password must be at least 6 characters long.")
    if role not in VALID_ROLES:
        raise ValidationError("Invalid role selected.")

    if User.objects.filter(email=email).exists():
        raise ValidationError("Email already registered.")

    # create_user uses CustomUserManager.create_user which calls set_password
    user = User.objects.create_user(
        email=email,
        password=password,
        full_name=full_name,
        role=role
    )
    return user

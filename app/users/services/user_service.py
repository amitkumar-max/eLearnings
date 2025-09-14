from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()

def create_user(full_name, email, password, role="student"):
    """
    Service layer function to handle user signup logic.
    """
    # ✅ Check email uniqueness
    if User.objects.filter(email=email).exists():
        raise ValidationError("Email already registered")

    # ✅ Use Django's built-in create_user (auto password hashing)
    user = User.objects.create_user(
        full_name=full_name,
        email=email,
        password=password,
        role=role
    )
    return user

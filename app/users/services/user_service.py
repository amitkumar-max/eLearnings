# app/users/services/user_service.py







from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from app.users.templates.users.models import User

def create_user(full_name, email, password):
    """
    Service layer function to handle user signup logic.
    """
    if User.objects.filter(email=email).exists():
        raise ValidationError("Email already registered")

    user = User(
        full_name=full_name,
        email=email,
        password=make_password(password)  # secure password hashing
    )
    user.save()
    return user

















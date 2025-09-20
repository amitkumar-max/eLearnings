from django.urls import path
from . import views

app_name = 'students'  # 👈 important

urlpatterns = [
    path("dashboard/", views.student_dashboard, name="dashboard"),  # name updated for clarity
]

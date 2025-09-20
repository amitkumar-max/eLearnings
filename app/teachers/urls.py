from django.urls import path
from . import views

app_name = 'teachers'  # namespace

urlpatterns = [
    path("dashboard/", views.teacher_dashboard, name="dashboard"),
    # baaki teacher views
]

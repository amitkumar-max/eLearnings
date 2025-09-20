# app/admin_panel/urls.py

from django.urls import path
from . import views

app_name = 'admins'  # namespace

urlpatterns = [
    path("dashboard/", views.admin_dashboard, name="dashboard"),
    # baaki admin views
]

# app/admin_panel/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.dashboard_view, name="admin_dashboard"),
    path("users/", views.user_list_view, name="admin_users"),
    path("reports/", views.reports_view, name="admin_reports"),
]



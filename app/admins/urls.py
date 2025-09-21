from django.urls import path
from . import views

app_name = "admins"

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("users/", views.users_management, name="users_management"),
    path("courses/", views.courses_management, name="courses_management"),
    path("payments/", views.payments, name="payments"),
    path("reports/", views.reports, name="reports"),
    path("support-tickets/", views.support_tickets, name="support_tickets"),
    path("site-settings/", views.site_settings, name="site_settings"),
    path("notifications/", views.notifications, name="notifications"),
]

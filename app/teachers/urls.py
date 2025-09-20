from django.urls import path
from . import views

app_name = "teachers"

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("announcements/", views.announcements, name="announcements"),
    path("assignments/", views.assignments, name="assignments"),
    path("assignments/<int:id>/", views.assignment_detail, name="assignment_detail"),
    path("courses/", views.courses, name="courses"),
    path("courses/<int:id>/", views.course_detail, name="course_detail"),
    path("grades/", views.grades, name="grades"),
    path("messages/", views.messages_view, name="messages"),
    path("notifications/", views.notifications, name="notifications"),
    path("profile/", views.profile, name="profile"),
    path("settings/", views.settings, name="settings"),
]

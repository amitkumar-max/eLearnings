from django.urls import path
from . import views

app_name = "students"

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("announcements/", views.announcements, name="announcements"),
    path("assignments/", views.assignments, name="assignments"),
    path("assignments/<int:id>/", views.assignment_detail, name="assignment_detail"),
    path("courses/", views.courses, name="courses"),
    path("courses/<int:id>/", views.course_detail, name="course_detail"),
    path("courses-list/", views.courses_list, name="courses_list"),
    path("my-courses/", views.my_courses, name="my_courses"),
    path("enrolled-courses/", views.enrolled_courses, name="enrolled_courses"),
    path("grades/", views.grades, name="grades"),
    path("login/", views.login_view, name="login"),
    path("messages/", views.messages_view, name="messages"),
    path("notifications/", views.notifications, name="notifications"),
    path("progress/", views.progress, name="progress"),
    path("settings/", views.settings, name="settings"),
    path("profile/", views.profile, name="profile"),
    path("edit-profile/", views.edit_profile, name="edit_profile"),
]

from django.urls import path
from . import views

app_name = "teachers"

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("announcements/", views.announcements, name="announcements"),
    path("announcements/<int:id>/", views.announcement_detail, name="announcement_detail"),
    path("courses/", views.courses, name="courses"),
    path("courses/<int:id>/", views.course_detail, name="course_detail"),
    path("create-course/", views.create_course, name="create_course"),
    path("edit-course/<int:id>/", views.edit_course, name="edit_course"),
    path("my-courses/", views.my_courses, name="my_courses"),
    path("grade-submission/", views.grade_submission, name="grade_submission"),
    path("manage-students/", views.manage_students, name="manage_students"),
    path("profile/", views.profile, name="profile"),
    path("edit-profile/", views.edit_profile, name="edit_profile"),
    path("messages/", views.messages_view, name="messages"),
    path("notifications/", views.notifications, name="notifications"),
    path("reports/", views.reports, name="reports"),
    path("settings/", views.settings, name="settings"),
]

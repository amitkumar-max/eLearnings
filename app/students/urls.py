from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView  # <- import this
app_name = "students"

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("announcements/", views.announcements, name="announcements"),
    path("assignments/", views.assignments, name="assignments"),
    path("assignments/<int:id>/", views.assignment_detail, name="assignment_detail"),
    path("courses/", views.courses, name="courses"),
    path("courses/<int:id>/", views.course_detail, name="course_detail"),
    path("courses-list/", views.courses_list, name="courses_list"),
    path("discussions/", views.discussions, name="discussions"),
    path("my-courses/", views.my_courses, name="my_courses"),
    path("enrolled-courses/", views.enrolled_courses, name="enrolled_courses"),
    path("grades/", views.grades, name="grades"),
    path("login/", views.login_view, name="login"),
    path("messages/", views.messages_view, name="messages"),
    path("notifications/", views.student_notifications, name="notifications"),
    path("fetch-notifications/", views.fetch_notifications, name="fetch_notifications"),
    path("progress/", views.progress, name="progress"),
    path("settings/", views.settings, name="settings"),
    path("profile/", views.profile, name="profile"),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('change-password/', views.change_password, name='change_password'),
    path('logout/', views.logout_view, name='logout'),  # use your logout_view
]

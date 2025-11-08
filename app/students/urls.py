from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),

    # Course-related views
    path('courses/', views.courses_list, name='courses_list'),
    path('courses/<str:slug>/start/', views.start_course, name='start_course'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
    path('enroll/<int:course_id>/', views.enroll_course, name='enroll_course'),

    path('my-courses/', views.my_courses, name='my_courses'),

    # Assignments
    path('assignments/', views.assignments, name='assignments'),
    path('assignments/<int:id>/', views.assignment_detail, name='assignment_detail'),

    # Notifications
    path('notifications/', views.student_notifications, name='notifications'),
    path('fetch-notifications/', views.fetch_notifications, name='fetch_notifications'),

    # Miscellaneous
    path('grades/', views.grades, name='grades'),
    path('messages/', views.messages_view, name='messages'),
    path('progress/', views.progress, name='progress'),
    path('settings/', views.settings, name='settings'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('discussions/', views.discussions, name='discussions'),
    path('announcements/', views.announcements, name='announcements'),
    path('logout/', views.logout_view, name='logout'),
    path('change-password/', views.change_password, name='change_password'),
]

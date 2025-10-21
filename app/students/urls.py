# from django.urls import path
# from . import views
# from django.contrib.auth.views import LogoutView  # <- import this
# app_name = "students"

# urlpatterns = [
#     path('enroll/<int:course_id>/', views.enroll_course, name='enroll_course'),
#     path("dashboard/", views.dashboard, name="dashboard"),
#     path("announcements/", views.announcements, name="announcements"),
#     path("assignments/", views.assignments, name="assignments"),
#     path("assignments/<int:id>/", views.assignment_detail, name="assignment_detail"),
#     path("courses/", views.courses, name="courses"),
#     path("courses/<int:id>/", views.course_detail, name="course_detail"),
#     path("courses-list/", views.courses_list, name="courses_list"),
#     path("discussions/", views.discussions, name="discussions"),
#     path("my-courses/", views.my_courses, name="my_courses"),
#     path("enrolled-courses/", views.enrolled_courses, name="enrolled_courses"),
#     path("grades/", views.grades, name="grades"),
#     path("login/", views.login_view, name="login"),
#     path("messages/", views.messages_view, name="messages"),
#     path("notifications/", views.student_notifications, name="notifications"),
#     path("fetch-notifications/", views.fetch_notifications, name="fetch_notifications"),
#     path("progress/", views.progress, name="progress"),
#     path("settings/", views.settings, name="settings"),
#     path("profile/", views.profile, name="profile"),
#     path('edit-profile/', views.edit_profile, name='edit_profile'),
#     path('change-password/', views.change_password, name='change_password'),
#     path('logout/', views.logout_view, name='logout'), 
#     path('start/<slug:slug>/', views.start_course, name='start_course'),
# path('lessons/', include('app.lessons.urls')),  # make sure this is included
# # use your logout_view
# ]



from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('courses/', views.courses_list, name='courses_list'),
    path('courses/<str:slug>/start/', views.start_course, name='start_course'),
    path('enroll_course/<str:slug>/', views.enroll_course, name='enroll_course'),
    path('my-courses/', views.my_courses, name='my_courses'),
    path('assignments/', views.assignments, name='assignments'),
    path('assignments/<int:id>/', views.assignment_detail, name='assignment_detail'),
    # path('notifications/', views.student_notifications, name='student_notifications'),
    path('fetch-notifications/', views.fetch_notifications, name='fetch_notifications'),
path('notifications/', views.student_notifications, name='notifications'),

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

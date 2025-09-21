from django.urls import path
from . import views

app_name = "notifications"

urlpatterns = [
    path("", views.notifications_list, name="list"),
    path("unread/", views.unread_notifications, name="unread"),
    path("dropdown/", views.notification_dropdown, name="dropdown"),  # include as fragment
    path("announcement/", views.system_announcements, name="announcements"),
    path("achievements/", views.achievement_notifications, name="achievements"),
    path("settings/", views.notification_settings, name="settings"),
    path("<int:pk>/", views.notification_detail, name="detail"),
]

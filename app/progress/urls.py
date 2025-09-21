from django.urls import path
from . import views

app_name = "progress"

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
]

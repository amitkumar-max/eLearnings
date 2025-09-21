from django.urls import path
from . import views

app_name = "progress"

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("list/", views.progress_list, name="progress_list"),
    path("result/<int:result_id>/", views.lesson_result_detail, name="result_detail"),
]

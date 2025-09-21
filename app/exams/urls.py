from django.urls import path
from . import views

app_name = "exams"

urlpatterns = [
    path("", views.exam_list, name="list"),
    path("<int:pk>/", views.ExamDetailView.as_view(), name="detail"),  # agar detail view chahiye
]

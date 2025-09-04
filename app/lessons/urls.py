from django.urls import path
from .views import LessonDetailView

urlpatterns = [
    path('<int:pk>/', LessonDetailView.as_view(), name='lesson_detail'),
]

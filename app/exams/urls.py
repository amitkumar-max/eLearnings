from django.urls import path
from .views import ExamListView, ExamDetailView

urlpatterns = [
    path('', ExamListView.as_view(), name='exam_list'),
    path('<int:pk>/', ExamDetailView.as_view(), name='exam_detail'),
]

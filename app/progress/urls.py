from django.urls import path
from .views import ProgressView

urlpatterns = [
    path('', ProgressView.as_view(), name='progress'),
]

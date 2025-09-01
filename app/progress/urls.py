from django.urls import path
from . import views  # ye ensure karo ke views import ho raha hai

urlpatterns = [
    path('', views.home, name='home'),  # home function aapke views.py me hona chahiye
]

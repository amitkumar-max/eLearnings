from django.urls import path
from . import views

app_name = 'downloads'

urlpatterns = [
    path('', views.file_list, name='file_list'),
    path('<int:file_id>/', views.file_detail, name='file_detail'),
    path('<int:file_id>/download/', views.download_file, name='download_file'),
]

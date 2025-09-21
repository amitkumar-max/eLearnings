from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('create/', views.blog_create, name='blog_create'),
    path('<int:blog_id>/edit/', views.blog_edit, name='blog_edit'),
    path('<int:blog_id>/comments/', views.blog_comments, name='blog_comments'),
]

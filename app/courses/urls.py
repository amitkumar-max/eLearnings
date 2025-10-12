
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView




app_name = "courses"

# urlpatterns = [
#     path('', views.course_list, name="course_list"),
#     path('categories/', views.categories, name="categories"),
#     # path('<int:course_id>/start/', views.course_start, name='course_start'),
#     path('categories/<slug:slug>/', views.category_courses, name="category_courses"),
#     path('<slug:slug>/', views.course_detail, name="course_detail"),
#     # path('<slug:slug>/player/<int:lesson_id>/', views.course_player, name="course_player"),
#     path('<slug:slug>/lesson/<int:lesson_id>/', views.course_player, name='course_player'),
#     # urls.py
# path('<slug:slug>/start/', views.start_course, name='start_course'),

# ]


urlpatterns = [
    path('', views.course_list, name="course_list"),
    path('categories/', views.categories, name="categories"),
    path('categories/<slug:slug>/', views.category_courses, name="category_courses"),
    path('<slug:slug>/', views.course_detail, name="course_detail"),
    path('<slug:slug>/lesson/<int:lesson_id>/', views.course_player, name='course_player'),
    path('<slug:slug>/start/', views.start_course, name='start_course'),  # <-- FIXED
path('accounts/login/', LoginView.as_view(template_name="users/login.html"), name="login"),


]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

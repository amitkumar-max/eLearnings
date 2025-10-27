# courses/urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "courses"

urlpatterns = [
    path('', views.course_list, name="course_list"),
    path('categories/', views.categories, name="categories"),
    path('categories/<slug:slug>/', views.category_courses, name="category_courses"),

    # ⚡ Lesson routes first (most specific)
    path('<slug:slug>/lesson/<int:lesson_id>/', views.course_player, name='course_player'),
    path('<slug:slug>/start/', views.start_course, name='start_course'),

    # 🧩 Course detail last (most generic)
    path('<slug:slug>/', views.course_detail, name="course_detail"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



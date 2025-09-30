from django.contrib import admin
from django.urls import path, include
from app.users import views as user_views
from django.conf import settings
from django.conf.urls.static import static
from pathlib import Path

# Define BASE_DIR for static files
BASE_DIR = Path(__file__).resolve().parent.parent
urlpatterns = [
    path('admin/', admin.site.urls),
    # User app
    path('users/', include('app.users.urls')),
    # Courses app
    path('courses/', include('app.courses.urls')),
    # Other apps
    path('students/', include('app.students.urls')),
    path('teachers/', include('app.teachers.urls')),
    path('admins/', include('app.admins.urls')),
    path('blogs/', include(('app.blogs.urls', 'blogs'), namespace='blogs')),
    path('downloads/', include(('app.downloads.urls', 'downloads'), namespace='downloads')),
    path('lessons/', include(('app.lessons.urls', 'lessons'), namespace='lessons')),
    path('payments/', include(('app.payments.urls', 'payments'), namespace='payments')),
    path('progress/', include(('app.progress.urls', 'progress'), namespace='progress')),
    path('notifications/', include(('app.notifications.urls', 'notifications'), namespace='notifications')),
    path('exams/', include(('app.exams.urls', 'exams'), namespace='exams')),
    # Home page
    path('', user_views.home, name='home'),
    # Policies app
    path('', include('app.policies.urls')),
]

# Serve static and media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=BASE_DIR / "static")

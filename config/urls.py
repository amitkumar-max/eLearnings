from django.contrib import admin
from django.urls import path, include
from app.users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('app.users.urls')),
    path('courses/', include('app.courses.urls')),
    path('students/', include('app.students.urls')),
    path('teachers/', include('app.teachers.urls')),
    path('admins/', include('app.admins.urls')),
    path('blogs/', include('app.blogs.urls', namespace='blogs')),
    path('downloads/', include('app.downloads.urls', namespace='downloads')),  # ✅ plural
    path('lessons/', include('app.lessons.urls', namespace='lessons')),
    path('payments/', include(('app.payments.urls', 'payments'), namespace='payments')),
    path('progress/', include('app.progress.urls', namespace='progress')),
    path('notifications/', include('app.notifications.urls', namespace='notifications')),
    path('exams/', include(('app.exams.urls', 'exams'), namespace='exams')),
    path('', user_views.home, name='home'),
    path('', include('app.policies.urls')),

]
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('courses/', include('courses.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=BASE_DIR / "static")


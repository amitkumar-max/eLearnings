# # from django.contrib import admin
# # from django.urls import path, include
# # from app.users import views as user_views
# # from django.conf import settings
# # from django.conf.urls.static import static
# # from pathlib import Path
# # from django.contrib.auth import views as auth_views   # ✅ Add this line
# # # Define BASE_DIR for static files
# # BASE_DIR = Path(__file__).resolve().parent.parent
# # urlpatterns = [
# #     path('admin/', admin.site.urls),
# #     # ✅ Explicit login/logout mapping
# #     path('users/login/', auth_views.LoginView.as_view(), name='login'),
# #     path('users/logout/', auth_views.LogoutView.as_view(), name='logout'),
   
# #     # User app
# #     path('users/', include('app.users.urls')),
# #     path('accounts/', include('django.contrib.auth.urls')),
# #     # Courses app
# #     path('courses/', include('app.courses.urls')),
# #     # Other apps
# #     path('students/', include('app.students.urls')),
# #     path('teachers/', include('app.teachers.urls')),
# #     path('admins/', include('app.admins.urls')),
# #     path('blogs/', include(('app.blogs.urls', 'blogs'), namespace='blogs')),
# #     path('downloads/', include(('app.downloads.urls', 'downloads'), namespace='downloads')),
# #     path('lessons/', include(('app.lessons.urls', 'lessons'), namespace='lessons')),
# #     path('payments/', include(('app.payments.urls', 'payments'), namespace='payments')),
# #     path('progress/', include(('app.progress.urls', 'progress'), namespace='progress')),
# #     path('notifications/', include(('app.notifications.urls', 'notifications'), namespace='notifications')),
# #     path('exams/', include(('app.exams.urls', 'exams'), namespace='exams')),
# #     # Home page
# #     path('', user_views.home, name='home'),
# #     # Policies app
# #     path('', include('app.policies.urls')),
# # ]

# # # Serve static and media files during development
# # if settings.DEBUG:
# #     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# #     urlpatterns += static(settings.STATIC_URL, document_root=BASE_DIR / "static")


# from django.contrib import admin
# from django.urls import path, include
# from django.contrib.auth import views as auth_views   # ✅ Import added
# from app.users import views as user_views
# from django.conf import settings
# from django.conf.urls.static import static
# from pathlib import Path

# BASE_DIR = Path(__file__).resolve().parent.parent

# urlpatterns = [
#     path('admin/', admin.site.urls),

#     # Explicit login/logout mapping
#     path('users/login/', auth_views.LoginView.as_view(), name='login'),
#     path('users/logout/', auth_views.LogoutView.as_view(), name='logout'),

#     # Other URL patterns
#     path('users/', include('app.users.urls')),
#     path('accounts/', include('django.contrib.auth.urls')),
#     path('courses/', include('app.courses.urls')),
#     path('students/', include('app.students.urls')),
#     path('teachers/', include('app.teachers.urls')),
#     path('admins/', include('app.admins.urls')),
#     path('blogs/', include(('app.blogs.urls', 'blogs'), namespace='blogs')),
#     path('downloads/', include(('app.downloads.urls', 'downloads'), namespace='downloads')),
#     path('lessons/', include(('app.lessons.urls', 'lessons'), namespace='lessons')),
#     path('payments/', include(('app.payments.urls', 'payments'), namespace='payments')),
#     path('progress/', include(('app.progress.urls', 'progress'), namespace='progress')),
#     path('notifications/', include(('app.notifications.urls', 'notifications'), namespace='notifications')),
#     path('exams/', include(('app.exams.urls', 'exams'), namespace='exams')),

# path(
#     'users/login/',
#     auth_views.LoginView.as_view(template_name='registration/login.html'),
#     name='login'
# ),
#     # Home page
#     path('', user_views.home, name='home'),
#     # Policies (if needed)
#     path('', include('app.policies.urls')),
# ]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#     urlpatterns += static(settings.STATIC_URL, document_root=BASE_DIR / "static")







from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views  # ✅ Correct import
from app.users import views as user_views
from django.conf import settings
from django.conf.urls.static import static
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

urlpatterns = [
    path('admin/', admin.site.urls),

    # ✅ Login/Logout mapping with template
    path(
        'users/login/',
        auth_views.LoginView.as_view(template_name='registration/login.html'),
        name='login'
    ),
    path(
        'users/logout/',
        auth_views.LogoutView.as_view(next_page='/users/login/'),
        name='logout'
    ),

    # User app URLs
    path('users/', include('app.users.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

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

    # Policies
    path('', include('app.policies.urls')),
]

# Serve static and media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=BASE_DIR / "static")

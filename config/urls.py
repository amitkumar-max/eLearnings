
# # # config/urls.py
# # from django.contrib import admin
# # from django.urls import path, include
# # # from users import views as user_views  # ADD THIS
# # from app.users import views as user_views

# # urlpatterns = [
# #     path('admin/', admin.site.urls),
# #     path('', user_views.home, name='home'),  # <-- 👈 ROOT URL
# #     path('courses/', include('app.courses.urls')),
# #     path('exams/', include('app.exams.urls')),
# #     path('lessons/', include('app.lessons.urls')),
# #     path('notifications/', include('app.notifications.urls')),
# #     path('payments/', include('app.payments.urls')),
# #     path('progress/', include('app.progress.urls')),
# #     path('users/', include('app.users.urls')),
# # ]








# # config/urls.py
# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('users/', include('app.users.urls')),
# ]



# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('users/', include('app.users.urls')),  # app/users routes
# ]

# # Development mode me media serve karne ke liye
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# from django.contrib import admin
# from django.urls import path, include
# from django.views.generic import RedirectView

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('users/', include('app.users.urls')),  # <- update path
#     path('', RedirectView.as_view(url='/users/', permanent=True)),  # root redirect
# ]


# from django.contrib import admin
# from django.urls import path, include
# from django.views.generic import RedirectView

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('users/', include('app.users.urls')),  # <- update path
#     path('', RedirectView.as_view(url='/users/', permanent=True)),  # root redirect
# ]




# from django.contrib import admin
# from django.urls import path, include
# from django.views.generic import RedirectView

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('users/', include('app.users.urls')),  # <- updated path
#     path('', RedirectView.as_view(url='/users/', permanent=True)),  # Root redirect
# ]



# from django.contrib import admin
# from django.urls import path, include
# from django.views.generic import RedirectView

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('users/', include('app.users.urls')),  # include users app
#     path('', RedirectView.as_view(url='/users/', permanent=True)),  # root redirect
# ]


# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('users/', include('app.users.urls', namespace='users')),  # ✅ namespace defined here
# ]


# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('users/', include('app.users.urls', namespace='users')),  # ✅ this is correct
# ]


# # config/urls.py
# from django.contrib import admin
# from django.urls import path, include
# from django.views.generic import TemplateView

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('users/', include('app.users.urls')),  # your app urls
#     path('', TemplateView.as_view(template_name='home.html'), name='home'),  # homepage route
# ]




# # config/urls.py
# from django.contrib import admin
# from django.urls import path, include
# from django.views.generic import TemplateView

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('users/', include('app.users.urls', namespace='users')),  # ✅ your namespace
#     path('', TemplateView.as_view(template_name='home.html'), name='home'),  # ✅ homepage route
# ]


from django.contrib import admin
from django.urls import path, include
from app.users import views   # ✅ import your views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('app.users.urls', namespace='users')),
    path('', views.home, name='home'),  # ✅ fix: use your home view
]




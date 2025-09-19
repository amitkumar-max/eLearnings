
# from django.contrib import admin
# from django.urls import path, include
# from app.users import views   # ✅ import your views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('users/', include('app.users.urls', namespace='users')),
#     path('', views.home, name='home'),  # ✅ fix: use your home view
# ]



from django.contrib import admin
from django.urls import path, include
from app.users import views  # home view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("users/", include("app.users.urls")),
    path("courses/", include("app.courses.urls")),  # courses namespace
]

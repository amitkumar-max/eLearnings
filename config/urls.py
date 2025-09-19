# from django.urls import path, include

# urlpatterns = [
#     path('users/', include('app.users.urls', namespace='users')),  # ✅ users namespace
#     path('courses/', include('app.courses.urls', namespace='courses')),  # ✅ courses namespace
# ]



from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")),
    path("courses/", include("courses.urls")),
    
    # 👇 root redirect ("/" -> "/courses/")
    path("", RedirectView.as_view(url="/courses/", permanent=False)),
]

# from django.urls import path, include

# urlpatterns = [
#     path('users/', include('app.users.urls', namespace='users')),  # ✅ users namespace
#     path('courses/', include('app.courses.urls', namespace='courses')),  # ✅ courses namespace
# ]



from django.contrib import admin
from django.urls import path, include
from app.users import views as user_views  # ya jahan home view ho

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("app.users.urls")),
    path("courses/", include("app.courses.urls")),
    
    # root "/" -> render home.html
    path("", user_views.home, name="home"),
]

from django.urls import path, include

urlpatterns = [
    path('users/', include('app.users.urls', namespace='users')),  # ✅ users namespace
    path('courses/', include('app.courses.urls', namespace='courses')),  # ✅ courses namespace
]

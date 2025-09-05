# # # # from django.urls import path
# # # # from . import views

# # # # urlpatterns = [
# # # #     path('', views.home, name='users-home'),
# # # # ]


# # # from django.urls import path
# # # from . import views

# # # urlpatterns = [
# # #     path('signup/', views.signup_view, name='signup'),
# # #     path('login/', views.login_view, name='login'),
# # #     path('logout/', views.logout_view, name='logout'),
# # #     path('profile/', views.profile_view, name='profile'),
# # # ]



# # # from django.urls import path
# # # from . import views

# # # urlpatterns = [
# # #     path('signup/', views.signup_view, name='signup'),
# # #     path('login/', views.login_view, name='login'),
# # #     path('logout/', views.logout_view, name='logout'),
# # #     path('profile/', views.profile_view, name='profile'),
# # # ]




# # from django.urls import path
# # from . import views

# # app_name = 'users'  # ✅ Ye zaroor hona chahiye

# # urlpatterns = [
# #     path('signup/', views.signup_view, name='signup'),
# #     path('login/', views.login_view, name='login'),
# #     path('logout/', views.logout_view, name='logout'),
# #     path('profile/', views.profile_view, name='profile'),
# # ]


# # from django.urls import path
# # from . import views

# # urlpatterns = [
# #     path('signup/', views.signup_view, name='signup'),
# #     path('login/', views.login_view, name='login'),
# # ]










# # from django.urls import path
# # from . import views

# # urlpatterns = [
# #     path('signup/', views.signup_view, name='signup'),
# #     path('login/', views.login_view, name='login'),
# # ]




# # from django.urls import path
# # from . import views

# # urlpatterns = [
# #     path('signup/', views.signup_view, name='signup'),
# #     path('login/', views.login_view, name='login'),
# # ]




# # from django.urls import path
# # from . import views
# # app_name = 'users'  # ✅ yeh define hona chahiye for namespacing
# # urlpatterns = [
# #     path('', views.home, name='home'),             # /users/
# #     path('signup/', views.signup_view, name='signup'),  # /users/signup/
# #     path('login/', views.login_view, name='login'),     # /users/login/
# #     path('profile/', views.profile_view, name='profile'), # /users/profile/
# # ]




# # from django.contrib import admin
# # from django.urls import path, include

# # urlpatterns = [
# #     path('admin/', admin.site.urls),
# #     path('users/', include('app.users.urls', namespace='users')),  # ✅ fixed path
# # ]



# from django.urls import path
# from . import views

# app_name = 'users'

# urlpatterns = [
#     path('', views.home, name='home'),                  # /users/
#     path('signup/', views.signup_view, name='signup'),  # /users/signup/
#     path('login/', views.login_view, name='login'),     # /users/login/
#     path('profile/', views.profile_view, name='profile'), # /users/profile/
#     path('logout/', views.logout_view, name='logout'),  # ✅ added logout URL
# ]


from django.urls import path
from .views import LoginView, LogoutView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]









from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('categories/', views.placeholder, name='categories'),
    path('lessons/', views.placeholder, name='lessons_list'),
    path('exams/', views.placeholder, name='exams_list'),
    path('payments/', views.placeholder, name='payments_history'),
    path('progress/', views.placeholder, name='progress_dashboard'),
    path('contact/', views.placeholder, name='contact'),
    path('support/faq/', views.placeholder, name='support_faq'),
    path('support/refund_policy/', views.placeholder, name='support_refund_policy'),
    path('support/privacy_policy/', views.placeholder, name='support_privacy_policy'),
    path('downloads/playstore/', views.placeholder, name='downloads_playstore'),
    path('downloads/appstore/', views.placeholder, name='downloads_appstore'),
]

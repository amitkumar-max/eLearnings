# policies/urls.py
from django.urls import path
from . import views

app_name = "policies"

urlpatterns = [
    path('faq/', views.faq_view, name='faq'),
    path('refund-policy/', views.refund_policy_view, name='refund_policy'),
    path('privacy-policy/', views.privacy_policy_view, name='privacy_policy'),
]

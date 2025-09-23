# app/payments/urls.py
from django.urls import path
from . import views

app_name = "payments"

urlpatterns = [
    path("checkout/<int:course_id>/", views.checkout, name="checkout"),
    path("success/<int:order_id>/", views.payment_success, name="success"),
    path("history/", views.payment_history, name="payment_history"),
]

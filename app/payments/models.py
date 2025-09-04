from django.db import models
from django.conf import settings
from django.utils import timezone
from courses.models import Course, TimeStampedModel

class Order(TimeStampedModel):
    ORDER_STATUS = [
        ("pending", "Pending"),
        ("paid", "Paid"),
        ("failed", "Failed"),
        ("refunded", "Refunded"),
        ("cancelled", "Cancelled"),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="orders")
    course = models.ForeignKey(Course, on_delete=models.PROTECT, related_name="orders")
    currency = models.CharField(max_length=10, default="INR")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=ORDER_STATUS, default="pending", db_index=True)
    meta = models.JSONField(default=dict, blank=True)

    def __str__(self):
        return f"Order #{self.pk} • {self.user} • {self.course.title} • {self.status}"


class Transaction(TimeStampedModel):
    PAYMENT_STATUS = [
        ("initiated", "Initiated"),
        ("success", "Success"),
        ("failed", "Failed"),
        ("refunded", "Refunded"),
    ]
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="transactions")
    gateway = models.CharField(max_length=30, default="razorpay")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10, default="INR")
    gateway_order_id = models.CharField(max_length=120, blank=True, db_index=True)
    gateway_payment_id = models.CharField(max_length=120, blank=True, db_index=True)
    gateway_signature = models.CharField(max_length=180, blank=True)
    status = models.CharField(max_length=20, choices=PAYMENT_STATUS, default="initiated", db_index=True)
    raw_payload = models.JSONField(default=dict, blank=True)
    processed_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Txn #{self.pk} • Order {self.order_id} • {self.status}"

    def mark_success(self, payload=None):
        self.status = "success"
        self.processed_at = timezone.now()
        if payload:
            self.raw_payload = payload
        self.save()

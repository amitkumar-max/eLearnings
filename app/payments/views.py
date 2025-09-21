from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Order, Transaction
from app.courses.models import Course
from django.utils import timezone

@login_required
def checkout(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    
    if request.method == "POST":
        # For now, we simulate a successful payment
        order = Order.objects.create(
            user=request.user,
            course=course,
            amount=course.price,
            status="paid",  # Assuming instant success for demo
        )
        txn = Transaction.objects.create(
            order=order,
            amount=order.amount,
            status="success",
            processed_at=timezone.now(),
        )
        return redirect("payments:success", order_id=order.pk)

    return render(request, "payments/checkout.html", {"course": course})

@login_required
def payment_success(request, order_id):
    order = get_object_or_404(Order, pk=order_id, user=request.user)
    return render(request, "payments/payment_success.html", {"order": order})

@login_required
def payment_history(request):
    orders = Order.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "payments/payment_history.html", {"orders": orders})

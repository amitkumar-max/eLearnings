from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, "admins/dashboard.html")

@login_required
def users_management(request):
    return render(request, "admins/users_management.html")

@login_required
def courses_management(request):
    return render(request, "admins/courses_management.html")

@login_required
def payments(request):
    return render(request, "admins/payments.html")

@login_required
def reports(request):
    return render(request, "admins/reports.html")

@login_required
def support_tickets(request):
    return render(request, "admins/support_tickets.html")

@login_required
def site_settings(request):
    return render(request, "admins/site_settings.html")

@login_required
def notifications(request):
    return render(request, "admins/notifications.html")

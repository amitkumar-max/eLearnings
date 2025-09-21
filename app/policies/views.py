# policies/views.py
from django.shortcuts import render

def faq_view(request):
    return render(request, "policies/faq.html")

def refund_policy_view(request):
    return render(request, "policies/refund_policy.html")

def privacy_policy_view(request):
    return render(request, "policies/privacy_policy.html")

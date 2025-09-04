from django.shortcuts import render
from django.views import View
from .models import Order, Transaction

class CheckoutView(View):
    def get(self, request):
        return render(request, 'payments/checkout.html')

    def post(self, request):
        # Payment gateway integration logic here
        return render(request, 'payments/success.html')

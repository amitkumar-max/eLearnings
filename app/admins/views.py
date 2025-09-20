from django.shortcuts import render

def admin_dashboard(request):
    # dashboard.html ko render karo
    return render(request, "admins/dashboard.html")

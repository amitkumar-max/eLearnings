from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def teacher_dashboard(request):
    # yahan teacher specific data fetch kar sakte ho
    return render(request, "teachers/dashboard.html", {
        "user": request.user
    })

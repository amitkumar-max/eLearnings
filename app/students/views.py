from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def student_dashboard(request):
    # yahan student specific data fetch kar sakte ho
    return render(request, "students/templates/students/dashboard.html", {
        "user": request.user
    })

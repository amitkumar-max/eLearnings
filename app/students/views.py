from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def student_dashboard(request):
    # student-specific data can be fetched here
    return render(request, "students/dashboard.html", {
        "user": request.user
    })

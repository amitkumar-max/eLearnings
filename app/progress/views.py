from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Result

@login_required
def progress_list(request):
    """
    Show all results/progress of the logged-in user
    """
    user_progress = Result.objects.filter(user=request.user)
    return render(request, 'progress/progress_list.html', {'progress': user_progress})

@login_required
def dashboard(request):
    """
    Dashboard page for progress overview
    """
    return render(request, "progress/dashboard.html")

@login_required
def lesson_result_detail(request, result_id):
    """
    Detailed view of a single result
    """
    result = get_object_or_404(Result, id=result_id, user=request.user)
    return render(request, 'progress/result_detail.html', {'result': result})

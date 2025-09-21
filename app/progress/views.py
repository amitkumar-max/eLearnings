from django.shortcuts import render
from django.views import View
from .models import Progress

class ProgressView(View):
    def get(self, request):
        user_progress = Progress.objects.filter(user=request.user)
        return render(request, 'progress/progress_list.html', {'progress': user_progress})



def dashboard(request):
    return render(request, "progress/progress_bar.html")

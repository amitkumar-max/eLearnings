from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import File

def file_list(request):
    files = File.objects.all().order_by('-created_at')
    return render(request, 'downloads/file_list.html', {'files': files})

def file_detail(request, file_id):
    file = get_object_or_404(File, id=file_id)
    return render(request, 'downloads/file_detail.html', {'file': file})

@login_required
def download_file(request, file_id):
    file = get_object_or_404(File, id=file_id)
    return render(request, 'downloads/download_confirmation.html', {'file': file})

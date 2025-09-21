from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import File

# ----------------------
# Public Views
# ----------------------

def file_list(request):
    """List all downloadable files"""
    files = File.objects.all().order_by('-created_at')
    return render(request, 'download/file_list.html', {'files': files})

def file_detail(request, file_id):
    """Show details about a single file"""
    file = get_object_or_404(File, id=file_id)
    return render(request, 'download/file_detail.html', {'file': file})

# ----------------------
# Login required for download
# ----------------------

@login_required
def download_file(request, file_id):
    """Handle actual file download"""
    file = get_object_or_404(File, id=file_id)
    # Optional: add tracking of downloads per user here
    # Example: file.download_count += 1; file.save()
    # Assuming files are stored in MEDIA_URL
    file_url = file.file.url
    return render(request, 'download/download_confirmation.html', {'file': file})

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # home.html aapke templates folder me hona chahiye

from django.shortcuts import render, get_object_or_404
from .models import Course  # assume Category model bhi hai

# 1️⃣ Courses list page
def course_list(request):
    courses = Course.objects.filter(is_published=True)
    return render(request, "courses/course_list.html", {"courses": courses})

# 2️⃣ Individual course detail page
def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug)
    return render(request, "courses/course_detail.html", {"course": course})

# 3️⃣ Categories page
def categories(request):
    categories = ["Python", "Web Development", "Data Science"]  # dummy
    return render(request, "courses/category_list.html", {"categories": categories})

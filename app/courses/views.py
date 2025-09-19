from django.shortcuts import render, get_object_or_404
from .models import Course, Lesson

# All courses
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

# Single course detail
def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    lessons = course.lessons.all().order_by('order')
    return render(request, 'courses/course_detail.html', {'course': course, 'lessons': lessons})

# Placeholder for categories (since template not ready)
def category_list(request):
    return render(request, "courses/category_list.html")

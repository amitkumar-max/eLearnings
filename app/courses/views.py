import os
from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, CourseInteraction, Category
from app.lessons.models import Lesson
from app.lessons.views import get_lesson_content_from_file
import os
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Course, CourseInteraction
from app.lessons.models import Lesson
from app.lessons.views import get_lesson_content_from_file

@login_required
def course_player(request, slug, lesson_id=None):
    course = get_object_or_404(Course, slug=slug)
    lessons = course.lessons_in_lessons_app.all()

    if not lessons.exists():
        return render(request, "courses/no_lessons.html", {"course": course})

    # Current lesson
    current_lesson = lessons.first() if not lesson_id else get_object_or_404(Lesson, id=lesson_id, course=course)

    # ✅ Fetch content safely
    lesson_content = get_lesson_content_from_file(current_lesson)

    # Handle interactions (like/save)
    interaction = None
    if request.user.is_authenticated:
        interaction, _ = CourseInteraction.objects.get_or_create(user=request.user, course=course)
        if request.method == "POST":
            if "like" in request.POST:
                interaction.liked = not interaction.liked
            if "save" in request.POST:
                interaction.saved = not interaction.saved
            interaction.save()
            return redirect("courses:course_player", slug=course.slug, lesson_id=current_lesson.id)

    # Progress %
    course_progress_percent = 0
    if lessons.exists() and interaction:
        total_lessons = lessons.count()
        completed = interaction.completed_lessons.count()
        course_progress_percent = int((completed / total_lessons) * 100)

    context = {
        "course": course,
        "lessons": lessons,
        "current_lesson": current_lesson,
        "lesson_content": lesson_content,   # ✅ consistent variable name
        "interaction": interaction,
        "completed_lessons": interaction.completed_lessons.values_list("id", flat=True) if interaction else [],
        "course_progress_percent": course_progress_percent,
        "course_slug": course.slug,
        "lesson_filename": os.path.basename(current_lesson.content_file.name) if current_lesson.content_file else f"lesson_{current_lesson.order_index}_placeholder.txt",
    }
    return render(request, "courses/course_player.html", context)
def course_list(request):
    courses = Course.objects.filter(is_published=True)
    return render(request, "courses/course_list.html", {"courses": courses})
def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug)
    interaction = None
    if request.user.is_authenticated:
        interaction, _ = CourseInteraction.objects.get_or_create(user=request.user, course=course)
    return render(request, "courses/course_detail.html", {"course": course, "interaction": interaction})
def categories(request):
    categories = [
        {"name": "Programming", "slug": "programming"},
        {"name": "Design", "slug": "design"},
        {"name": "Business", "slug": "business"},
        {"name": "Science", "slug": "science"},
        {"name": "Mathematics", "slug": "mathematics"},
        {"name": "Languages", "slug": "languages"},
    ]
    return render(request, "courses/category_list.html", {"categories": categories})
def category_courses(request, slug):
    category = get_object_or_404(Category, slug=slug)
    courses = Course.objects.filter(category=category, is_published=True)
    return render(request, "courses/course_list.html", {
        "courses": courses,
        "category_name": category.name
    })



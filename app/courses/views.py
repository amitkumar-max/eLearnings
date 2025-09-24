from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, CourseInteraction
from app.lessons.models import Lesson
from app.lessons.views import get_lesson_content_from_file

# 1️⃣ Courses list page
def course_list(request):
    courses = Course.objects.filter(is_published=True)
    return render(request, "courses/course_list.html", {"courses": courses})

def categories(request):
    categories = ["Python", "Web Development", "Data Science"]  # ya database se fetch kar sakte ho
    return render(request, "courses/category_list.html", {"categories": categories})

# 2️⃣ Individual course detail page
def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug)
    
    interaction = None
    if request.user.is_authenticated:
        interaction, _ = CourseInteraction.objects.get_or_create(user=request.user, course=course)
    
    return render(request, "courses/course_detail.html", {
        "course": course,
        "interaction": interaction
    })
# 3️⃣ Lesson Player page (Fixed)

def course_player(request, slug, lesson_id=None):
    course = get_object_or_404(Course, slug=slug)
    lessons = course.lessons_in_lessons_app.all()

    if not lessons.exists():
        return render(request, "courses/no_lessons.html", {"course": course})

    current_lesson = lessons.first() if not lesson_id else get_object_or_404(Lesson, id=lesson_id, course=course)

    # Use the new loader
    lesson_content = get_lesson_content_from_file(current_lesson)

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

    course_progress_percent = int(
        (interaction.completed_lessons.count() / lessons.count()) * 100
    ) if lessons.exists() and interaction else 0

    context = {
        "course": course,
        "lessons": lessons,
        "current_lesson": current_lesson,
        "lesson_content": lesson_content,
        "interaction": interaction,
        "completed_lessons": interaction.completed_lessons.values_list("id", flat=True) if interaction else [],
        "course_progress_percent": course_progress_percent,
    }
    return render(request, "courses/course_player.html", context)

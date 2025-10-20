# import os
# from django.shortcuts import render, get_object_or_404, redirect
# from .models import Course, CourseInteraction, Category
# from app.lessons.models import Lesson
# from app.lessons.views import get_lesson_content_from_file
# import os
# from django.shortcuts import render, get_object_or_404, redirect
# from django.contrib.auth.decorators import login_required
# from .models import Course, CourseInteraction
# from app.lessons.models import Lesson
# from app.lessons.views import get_lesson_content_from_file
# from django.contrib.auth.decorators import login_required

# # def course_player(request, slug, lesson_id=None):
# #     course = get_object_or_404(Course, slug=slug)
# #     lessons = course.lessons_in_lessons_app.all()

# #     if not lessons.exists():
# #         return render(request, "courses/no_lessons.html", {"course": course})

# #     # Current lesson
# #     current_lesson = lessons.first() if not lesson_id else get_object_or_404(Lesson, id=lesson_id, course=course)

# #     # ✅ Fetch content safely
# #     lesson_content = get_lesson_content_from_file(current_lesson)

# #     # Handle interactions (like/save)
# #     interaction = None
# #     if request.user.is_authenticated:
# #         interaction, _ = CourseInteraction.objects.get_or_create(user=request.user, course=course)
# #         if request.method == "POST":
# #             if "like" in request.POST:
# #                 interaction.liked = not interaction.liked
# #             if "save" in request.POST:
# #                 interaction.saved = not interaction.saved
# #             interaction.save()
# #             return redirect("courses:course_player", slug=course.slug, lesson_id=current_lesson.id)

# #     # Progress %
# #     course_progress_percent = 0
# #     if lessons.exists() and interaction:
# #         total_lessons = lessons.count()
# #         completed = interaction.completed_lessons.count()
# #         course_progress_percent = int((completed / total_lessons) * 100)

# #     context = {
# #         "course": course,
# #         "lessons": lessons,
# #         "current_lesson": current_lesson,
# #         "lesson_content": lesson_content,   # ✅ consistent variable name
# #         "interaction": interaction,
# #         "completed_lessons": interaction.completed_lessons.values_list("id", flat=True) if interaction else [],
# #         "course_progress_percent": course_progress_percent,
# #         "course_slug": course.slug,
# #         "lesson_filename": os.path.basename(current_lesson.content_file.name) if current_lesson.content_file else f"lesson_{current_lesson.order_index}_placeholder.txt",
# #     }
# #     return render(request, "courses/course_player.html", context)

# from django.shortcuts import render, get_object_or_404
# from .models import Course, Lesson

# @login_required
# def course_player(request, slug, lesson_id):
#     course = get_object_or_404(Course, slug=slug)
#     lessons = course.lessons.all()
#     current_lesson = get_object_or_404(Lesson, id=lesson_id, course=course)

#     # Example: completed lessons
#     completed_lessons = request.user.completed_lessons.filter(course=course).values_list('id', flat=True)

#     # Progress calculation
#     total = lessons.count()
#     completed = len(completed_lessons)
#     course_progress_percent = int((completed / total) * 100) if total else 0

#     context = {
#         'course': course,
#         'lessons': lessons,
#         'current_lesson': current_lesson,
#         'completed_lessons': completed_lessons,
#         'course_progress_percent': course_progress_percent,
#         'lesson_filename': current_lesson.filename,
#         'lesson_content': current_lesson.content,
#         'progress': int((current_lesson.id / total) * 100),
#         'interaction': current_lesson.get_interaction(request.user),
#     }

#     return render(request, 'courses/course_player.html', context)



# @login_required
# def start_course(request, slug):
#     course = get_object_or_404(Course, slug=slug)
#     return render(request, "courses/start_course.html", {"course": course})

# def course_list(request):
#     courses = Course.objects.filter(is_published=True)
#     return render(request, "courses/course_list.html", {"courses": courses})
# def course_detail(request, slug):
#     course = get_object_or_404(Course, slug=slug)
#     interaction = None
#     if request.user.is_authenticated:
#         interaction, _ = CourseInteraction.objects.get_or_create(user=request.user, course=course)
#     return render(request, "courses/course_detail.html", {"course": course, "interaction": interaction})
# def categories(request):
#     categories = [
#         {"name": "Programming", "slug": "programming"},
#         {"name": "Design", "slug": "design"},
#         {"name": "Business", "slug": "business"},
#         {"name": "Science", "slug": "science"},
#         {"name": "Mathematics", "slug": "mathematics"},
#         {"name": "Languages", "slug": "languages"},
#     ]
#     return render(request, "courses/category_list.html", {"categories": categories})
# def category_courses(request, slug):
#     category = get_object_or_404(Category, slug=slug)
#     courses = Course.objects.filter(category=category, is_published=True)
#     return render(request, "courses/course_list.html", {
#         "courses": courses,
#         "category_name": category.name
#     })


# # DB_PASSWORD=mnuRqC7I0hFPETVy2R8CzhwpGKvYVIcR

import os
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Course, CourseInteraction, Category
from app.lessons.models import Lesson


# --------------------------
# COURSE START VIEW
# --------------------------
@login_required
def start_course(request, slug):
    """
    Display the start_course page with all lessons of a course.
    """
    course = get_object_or_404(Course, slug=slug)
    lessons = course.lessons.order_by("order_index")

    # Fetch user's progress
    interaction = None
    completed_lessons = []
    if request.user.is_authenticated:
        interaction, _ = CourseInteraction.objects.get_or_create(
            user=request.user, course=course
        )
        completed_lessons = interaction.completed_lessons.values_list("id", flat=True)

    # Calculate progress percentage
    total = lessons.count()
    completed = len(completed_lessons)
    course_progress_percent = int((completed / total) * 100) if total else 0

    context = {
        "course": course,
        "lessons": lessons,
        "completed_lessons": completed_lessons,
        "course_progress_percent": course_progress_percent,
        "interaction": interaction,
    }
    return render(request, "courses/start_course.html", context)


# --------------------------
# COURSE PLAYER VIEW
# --------------------------
@login_required
def course_player(request, lesson_id):
    """
    Display a single lesson with navigation and progress tracking.
    """
    lesson = get_object_or_404(Lesson, id=lesson_id)
    course = lesson.course
    lessons = course.lessons.order_by("order_index")

    # Determine previous/next lessons
    lesson_list = list(lessons)
    idx = lesson_list.index(lesson)
    previous_lesson = lesson_list[idx - 1] if idx > 0 else None
    next_lesson = lesson_list[idx + 1] if idx < len(lesson_list) - 1 else None

    # Fetch user's completed lessons
    interaction = None
    completed_lessons = []
    if request.user.is_authenticated:
        interaction, _ = CourseInteraction.objects.get_or_create(
            user=request.user, course=course
        )
        completed_lessons = interaction.completed_lessons.values_list("id", flat=True)

    # Calculate progress percentage
    total = lessons.count()
    completed = len(completed_lessons)
    course_progress_percent = int((completed / total) * 100) if total else 0

    context = {
        "course": course,
        "current_lesson": lesson,
        "lessons": lessons,
        "previous_lesson": previous_lesson,
        "next_lesson": next_lesson,
        "lesson_content": lesson.content_text,
        "completed_lessons": completed_lessons,
        "course_progress_percent": course_progress_percent,
        "interaction": interaction,
    }

    return render(request, "courses/course_player.html", context)


# --------------------------
# COURSE LIST VIEW
# --------------------------
def course_list(request):
    """
    List all published courses.
    """
    courses = Course.objects.filter(is_published=True)
    return render(request, "courses/course_list.html", {"courses": courses})


# --------------------------
# COURSE DETAIL VIEW
# --------------------------
def course_detail(request, slug):
    """
    Show course detail page.
    """
    course = get_object_or_404(Course, slug=slug)
    interaction = None

    if request.user.is_authenticated:
        interaction, _ = CourseInteraction.objects.get_or_create(
            user=request.user, course=course
        )

    return render(
        request,
        "courses/course_detail.html",
        {"course": course, "interaction": interaction},
    )


# --------------------------
# CATEGORY LIST VIEW
# --------------------------
def categories(request):
    """
    Show all categories.
    """
    categories = [
        {"name": "Programming", "slug": "programming"},
        {"name": "Design", "slug": "design"},
        {"name": "Business", "slug": "business"},
        {"name": "Science", "slug": "science"},
        {"name": "Mathematics", "slug": "mathematics"},
        {"name": "Languages", "slug": "languages"},
    ]
    return render(request, "courses/category_list.html", {"categories": categories})


# --------------------------
# CATEGORY COURSES VIEW
# --------------------------
def category_courses(request, slug):
    """
    List courses for a specific category.
    """
    category = get_object_or_404(Category, slug=slug)
    courses = Course.objects.filter(category=category, is_published=True)

    return render(
        request,
        "courses/course_list.html",
        {"courses": courses, "category_name": category.name},
    )

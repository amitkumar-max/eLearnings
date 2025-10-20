import os
import glob
import json

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse

from app.courses.models import Course
from .models import (
    Lesson,
    LessonProgress,
    QuizQuestion,
    QuizOption,
    LessonComment,
    LessonResource,
    LessonFeedback,
)


# --------------------------
# COURSE START VIEW
# --------------------------
def start_course(request, slug):
    course = get_object_or_404(Course, slug=slug)
    lessons = course.lessons.all().order_by("order_index")
    return render(
        request,
        "courses/course_start.html",
        {
            "course": course,
            "lessons": lessons,
            "current_lesson": lessons.first() if lessons.exists() else None,
        },
    )


# --------------------------
# FILE CONTENT HANDLER
# --------------------------
def get_lesson_content_from_file(lesson, return_path=False):
    normalized_slug = lesson.course.slug.lower().replace(" ", "-")
    paths_to_try = [
        os.path.join(settings.MEDIA_ROOT, "lessons", normalized_slug),
        os.path.join(settings.BASE_DIR, "app", "lessons", "content", normalized_slug),
    ]

    for folder_path in paths_to_try:
        if not os.path.exists(folder_path):
            continue

        pattern = f"lesson_{lesson.order_index}_*.txt"
        matched_files = glob.glob(os.path.join(folder_path, pattern))
        if matched_files:
            path = matched_files[0]
            try:
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
                content = content.replace("\n\n", "</p><p>").replace("\n", "<br>")
                html_content = f"<p>{content}</p>"
                return (html_content, path) if return_path else html_content
            except Exception as e:
                print(f"[Error reading file] {e}")
                return "Lesson content not available."

    # Placeholder fallback
    placeholder_path = os.path.join(
        settings.BASE_DIR, "app", "lessons", "content", "placeholder.txt"
    )
    if os.path.exists(placeholder_path):
        with open(placeholder_path, "r", encoding="utf-8") as f:
            content = f.read()
        content = content.replace("\n\n", "</p><p>").replace("\n", "<br>")
        html_content = f"<p>{content}</p>"
        return (html_content, placeholder_path) if return_path else html_content

    return (
        ("Lesson content not found.", None)
        if return_path
        else "Lesson content not found."
    )


# --------------------------
# LESSON LIST VIEW
# --------------------------
def lesson_list(request):
    lessons = Lesson.objects.all().order_by("created_at")
    return render(request, "lessons/lesson_list.html", {"lessons": lessons})


# --------------------------
# LESSON DETAIL VIEW
# --------------------------
@login_required
def lesson_detail(request, course_slug, lesson_filename):
    """
    Reads lesson content using helper and tracks user progress.
    """
    lesson = get_object_or_404(
        Lesson, course__slug=course_slug, slug=lesson_filename.replace(".txt", "")
    )
    lesson_content = get_lesson_content_from_file(lesson)

    progress = 0
    if request.user.is_authenticated:
        obj, _ = LessonProgress.objects.get_or_create(
            user=request.user,
            course_slug=course_slug,
            lesson_filename=lesson_filename,
            defaults={"progress": 0},
        )
        progress = obj.progress

    context = {
        "current_lesson": lesson,
        "lesson_content_html": lesson_content,
        "course_slug": course_slug,
        "lesson_filename": lesson_filename,
        "progress": progress,
    }
    return render(request, "courses/course_player.html", context)


# --------------------------
# LESSON PROGRESS API
# --------------------------
def lesson_progress(request, course_slug, lesson_filename):
    if request.method == "POST" and request.user.is_authenticated:
        data = json.loads(request.body)
        progress = data.get("progress", 0)

        obj, created = LessonProgress.objects.get_or_create(
            user=request.user,
            course_slug=course_slug,
            lesson_filename=lesson_filename,
            defaults={"progress": progress},
        )
        if not created:
            obj.progress = progress
            obj.save()

        return JsonResponse({"status": "ok", "progress": obj.progress})

    return JsonResponse({"status": "error"}, status=400)


# --------------------------
# LESSON QUIZ VIEW
# --------------------------
def lesson_quiz(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    questions = QuizQuestion.objects.filter(lesson=lesson)

    if request.method == "POST":
        return redirect("lessons:lesson_progress", lesson_id=lesson.id)

    return render(
        request, "lessons/lesson_quiz.html", {"lesson": lesson, "quiz_questions": questions}
    )


# --------------------------
# LESSON COMMENTS VIEW
# --------------------------
def lesson_comments(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    comments = LessonComment.objects.filter(lesson=lesson).order_by("-created_at")

    if request.method == "POST":
        text = request.POST.get("text")
        if text:
            LessonComment.objects.create(user=request.user, lesson=lesson, comment=text)
            return redirect("lessons:lesson_comments", lesson_id=lesson.id)

    return render(
        request, "lessons/lesson_comments.html", {"lesson": lesson, "comments": comments}
    )


# --------------------------
# LESSON RESOURCES VIEW
# --------------------------
def lesson_resources(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    resources = LessonResource.objects.filter(lesson=lesson)
    return render(
        request, "lessons/lesson_resources.html", {"lesson": lesson, "resources": resources}
    )


# --------------------------
# LESSON FEEDBACK VIEW
# --------------------------
def lesson_feedback(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    if request.method == "POST":
        comments = request.POST.get("comments")
        LessonFeedback.objects.create(user=request.user, lesson=lesson, feedback=comments)
        return redirect("lessons:lesson_list")

    return render(request, "lessons/lesson_feedback.html", {"lesson": lesson})

import os
import glob
import json
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import (
    Lesson, LessonProgress, QuizQuestion, QuizOption,
    LessonComment, LessonResource, LessonFeedback
)
import os
import glob
from django.conf import settings

def get_lesson_content_from_file(lesson, return_path=False):
    normalized_slug = lesson.course.slug.lower().replace(" ", "-")
    paths_to_try = [
        os.path.join(settings.MEDIA_ROOT, 'lessons', normalized_slug),
        os.path.join(settings.BASE_DIR, 'app', 'lessons', 'content', normalized_slug),
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
                return (f"<p>{content}</p>", path) if return_path else f"<p>{content}</p>"
            except Exception as e:
                print(f"[Error reading file] {e}")
                return "Lesson content not available."

    # Placeholder fallback
    placeholder_path = os.path.join(settings.BASE_DIR, 'app', 'lessons', 'content', 'placeholder.txt')
    if os.path.exists(placeholder_path):
        with open(placeholder_path, "r", encoding="utf-8") as f:
            content = f.read()
        content = content.replace("\n\n", "</p><p>").replace("\n", "<br>")
        return (f"<p>{content}</p>", placeholder_path) if return_path else f"<p>{content}</p>"

    return ("Lesson content not found.", None) if return_path else "Lesson content not found."
def lesson_list(request):
    lessons = Lesson.objects.all().order_by('created_at')
    return render(request, 'lessons/lesson_list.html', {'lessons': lessons})

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Lesson, LessonProgress
from app.lessons.views import get_lesson_content_from_file

@login_required
def lesson_detail(request, course_slug, lesson_filename):
    """
    Safe old-style lesson detail view:
    Reads lesson content using helper, works with login_required.
    """
    # Try to find Lesson object first
    lesson = get_object_or_404(Lesson, course__slug=course_slug, slug=lesson_filename.replace(".txt",""))

    # ✅ Fetch lesson content safely
    lesson_content = get_lesson_content_from_file(lesson)

    # Progress tracking
    progress = 0
    if request.user.is_authenticated:
        obj, _ = LessonProgress.objects.get_or_create(
            user=request.user,
            course_slug=course_slug,
            lesson_filename=lesson_filename,
            defaults={"progress": 0}
        )
        progress = obj.progress

    context = {
        "current_lesson": lesson,
        "lesson_content": lesson_content,   # consistent variable
        "course_slug": course_slug,
        "lesson_filename": lesson_filename,
        "progress": progress,
    }
    return render(request, "courses/course_player.html", context)
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
def lesson_quiz(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    questions = QuizQuestion.objects.filter(lesson=lesson)
    if request.method == 'POST':
        return redirect('lessons:lesson_progress', lesson_id=lesson.id)
    return render(request, 'lessons/lesson_quiz.html', {'lesson': lesson, 'quiz_questions': questions})
def lesson_comments(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    comments = LessonComment.objects.filter(lesson=lesson).order_by('-created_at')
    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            LessonComment.objects.create(user=request.user, lesson=lesson, comment=text)
            return redirect('lessons:lesson_comments', lesson_id=lesson.id)
    return render(request, 'lessons/lesson_comments.html', {'lesson': lesson, 'comments': comments})
def lesson_resources(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    resources = LessonResource.objects.filter(lesson=lesson)
    return render(request, 'lessons/lesson_resources.html', {'lesson': lesson, 'resources': resources})
def lesson_feedback(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    if request.method == 'POST':
        comments = request.POST.get('comments')
        LessonFeedback.objects.create(user=request.user, lesson=lesson, feedback=comments)
        return redirect('lessons:lesson_list')
    return render(request, 'lessons/lesson_feedback.html', {'lesson': lesson})



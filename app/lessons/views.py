# from django.shortcuts import render, get_object_or_404, redirect
# from .models import Lesson, QuizQuestion, QuizOption, LessonProgress, LessonComment, LessonResource, LessonFeedback
# import os
# from django.conf import settings
# from .models import LessonProgress
# from django.http import JsonResponse
# import json
# # lessons/views.py
# import os
# import glob
# from django.conf import settings

# def get_lesson_content_from_file(lesson):
#     """
#     Reads the lesson content from MEDIA_ROOT/lessons/<course-slug>/ folder.
#     Matches file starting with lesson_<order_index>_*.txt
#     Returns the text content or a fallback message.
#     """
#     folder_path = os.path.join(settings.MEDIA_ROOT, 'lessons', lesson.course.slug)
    
#     # Ensure folder exists
#     if not os.path.exists(folder_path):
#         return "Lesson content not found."

#     # Match file pattern
#     pattern = f"lesson_{lesson.order_index}_*.txt"
#     matched_files = glob.glob(os.path.join(folder_path, pattern))

#     if matched_files:
#         try:
#             with open(matched_files[0], "r", encoding="utf-8") as f:
#                 content = f.read()
#             # Optional: replace double line breaks with <p> tags for template rendering
#             content = content.replace("\n\n", "</p><p>").replace("\n", "<br>")
#             return f"<p>{content}</p>"
#         except Exception as e:
#             return f"Error reading lesson content: {str(e)}"
#     return "Lesson content not found."

# # -----------------------------
# # All_Lessons List
# # -----------------------------
# def lesson_list(request):
#     lessons = Lesson.objects.all().order_by('created_at')
#     return render(request, 'lessons/lesson_list.html', {'lessons': lessons})



# # -----------------------------
# # Lesson Quiz
# # -----------------------------
# def lesson_quiz(request, lesson_id):
#     lesson = get_object_or_404(Lesson, id=lesson_id)
#     questions = QuizQuestion.objects.filter(lesson=lesson)
    
#     if request.method == 'POST':
#         # handle quiz submission logic
#         # calculate score, save results, redirect to progress
#         return redirect('lessons:lesson_progress', lesson_id=lesson.id)
    
#     return render(request, 'lessons/lesson_quiz.html', {'lesson': lesson, 'quiz_questions': questions})



# def lesson_detail(request, course_slug, lesson_filename):
#     # Path to lesson file
#     lessons_dir = os.path.join(settings.BASE_DIR, "app", "lessons", "content", course_slug)
#     file_path = os.path.join(lessons_dir, lesson_filename)

#     content = ""
#     if os.path.exists(file_path):
#         with open(file_path, "r", encoding="utf-8") as f:
#             content = f.read()
#     else:
#         content = "Lesson content not found."

#     # Fetch or create progress record
#     progress = 0
#     if request.user.is_authenticated:
#         obj, _ = LessonProgress.objects.get_or_create(
#             user=request.user,
#             course_slug=course_slug,
#             lesson_filename=lesson_filename,
#             defaults={"progress": 0}
#         )
#         progress = obj.progress

#     return render(request, "courses/course_player.html", {
#         "content": content,
#         "course_slug": course_slug,
#         "lesson_filename": lesson_filename,
#         "progress": progress,
#     })




# # -----------------------------
# # Lesson Progress
# # -----------------------------
# def lesson_progress(request, course_slug, lesson_filename):
#     if request.method == "POST" and request.user.is_authenticated:
#         data = json.loads(request.body)
#         progress = data.get("progress", 0)

#         obj, created = LessonProgress.objects.get_or_create(
#             user=request.user,
#             course_slug=course_slug,
#             lesson_filename=lesson_filename,
#             defaults={"progress": progress},
#         )
#         if not created:
#             obj.progress = progress
#             obj.save()

#         return JsonResponse({"status": "ok", "progress": obj.progress})

#     return JsonResponse({"status": "error"}, status=400)
# # -----------------------------
# # Lesson Comments
# # -----------------------------
# def lesson_comments(request, lesson_id):
#     lesson = get_object_or_404(Lesson, id=lesson_id)
#     comments = LessonComment.objects.filter(lesson=lesson).order_by('-created_at')
    
#     if request.method == 'POST':
#         text = request.POST.get('text')
#         if text:
#             LessonComment.objects.create(user=request.user, lesson=lesson, text=text)
#             return redirect('lessons:lesson_comments', lesson_id=lesson.id)
    
#     return render(request, 'lessons/lesson_comments.html', {'lesson': lesson, 'comments': comments})

# # -----------------------------
# # Lesson Resources
# # -----------------------------
# def lesson_resources(request, lesson_id):
#     lesson = get_object_or_404(Lesson, id=lesson_id)
#     resources = LessonResource.objects.filter(lesson=lesson)
#     return render(request, 'lessons/lesson_resources.html', {'lesson': lesson, 'resources': resources})

# # -----------------------------
# # Lesson Feedback
# # -----------------------------
# def lesson_feedback(request, lesson_id):
#     lesson = get_object_or_404(Lesson, id=lesson_id)
    
#     if request.method == 'POST':
#         rating = request.POST.get('rating')
#         comments = request.POST.get('comments')
#         LessonFeedback.objects.create(user=request.user, lesson=lesson, rating=rating, comments=comments)
#         return redirect('lessons:lesson_list')
    
#     return render(request, 'lessons/lesson_feedback.html', {'lesson': lesson})






import os
import glob
import json
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Lesson, LessonProgress, QuizQuestion, QuizOption, LessonComment, LessonResource, LessonFeedback

# -----------------------------
# Lesson Content Loader

def get_lesson_content_from_file(lesson):
    """
    Reads lesson content from:
    1. MEDIA_ROOT/lessons/<normalized-course-slug>/
    2. fallback: app/lessons/content/<normalized-course-slug>/
    Returns HTML-safe content.
    """
    # Normalize slug to lowercase and hyphen format (folder-safe)
    normalized_slug = lesson.course.slug.lower().replace(" ", "-")

    paths_to_try = [
        os.path.join(settings.MEDIA_ROOT, 'lessons', normalized_slug),
        os.path.join(settings.BASE_DIR, 'app', 'lessons', 'content', normalized_slug),
    ]

    for folder_path in paths_to_try:
        if not os.path.exists(folder_path):
            continue

        # Pattern to match lesson files
        pattern = f"lesson_{lesson.order_index}_*.txt"
        matched_files = glob.glob(os.path.join(folder_path, pattern))

        # Debugging (optional, remove in production)
        # print("Checking folder:", folder_path)
        # print("Pattern:", pattern)
        # print("Matched files:", matched_files)

        if matched_files:
            try:
                with open(matched_files[0], "r", encoding="utf-8") as f:
                    content = f.read()
                # Convert line breaks to HTML
                content = content.replace("\n\n", "</p><p>").replace("\n", "<br>")
                return f"<p>{content}</p>"
            except Exception as e:
                return f"Error reading content: {str(e)}"

    # Final fallback: placeholder file in content folder
    placeholder_path = os.path.join(settings.BASE_DIR, 'app', 'lessons', 'content', 'placeholder.txt')
    if os.path.exists(placeholder_path):
        with open(placeholder_path, "r", encoding="utf-8") as f:
            content = f.read()
        content = content.replace("\n\n", "</p><p>").replace("\n", "<br>")
        return f"<p>{content}</p>"

    return "Lesson content not found."
# -----------------------------
# Lesson List
# -----------------------------
def lesson_list(request):
    lessons = Lesson.objects.all().order_by('created_at')
    return render(request, 'lessons/lesson_list.html', {'lessons': lessons})

# -----------------------------
# Lesson Detail / Player
# -----------------------------
def lesson_detail(request, course_slug, lesson_filename):
    lessons_dir = os.path.join(settings.BASE_DIR, "app", "lessons", "content", course_slug)
    file_path = os.path.join(lessons_dir, lesson_filename)

    content = ""
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
    else:
        content = "Lesson content not found."

    progress = 0
    if request.user.is_authenticated:
        obj, _ = LessonProgress.objects.get_or_create(
            user=request.user,
            course_slug=course_slug,
            lesson_filename=lesson_filename,
            defaults={"progress": 0}
        )
        progress = obj.progress

    return render(request, "courses/course_player.html", {
        "content": content,
        "course_slug": course_slug,
        "lesson_filename": lesson_filename,
        "progress": progress,
    })

# -----------------------------
# Lesson Progress (AJAX)
# -----------------------------
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

# -----------------------------
# Quiz, Comments, Resources, Feedback
# -----------------------------
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
        rating = request.POST.get('rating')
        comments = request.POST.get('comments')
        LessonFeedback.objects.create(user=request.user, lesson=lesson, feedback=comments)
        return redirect('lessons:lesson_list')
    return render(request, 'lessons/lesson_feedback.html', {'lesson': lesson})

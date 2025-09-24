from django.shortcuts import render, get_object_or_404, redirect
from .models import Lesson, QuizQuestion, QuizOption, LessonProgress, LessonComment, LessonResource, LessonFeedback
import os
from django.conf import settings


def get_lesson_content_from_file(lesson):
    """
    Reads the lesson content from lessons/content/<course-slug>/ folder.
    Matches file starting with lesson_<order_index>_*.txt
    """
    import glob
    import os

    folder_path = os.path.join(settings.BASE_DIR, "lessons", "content", lesson.course.slug)
    pattern = f"lesson_{lesson.order_index}_*.txt"
    matched_files = glob.glob(os.path.join(folder_path, pattern))
    
    if matched_files:
        with open(matched_files[0], "r", encoding="utf-8") as f:
            return f.read()
    return "Lesson content not found."



# -----------------------------
# All Lessons List
# -----------------------------
def lesson_list(request):
    lessons = Lesson.objects.all().order_by('created_at')
    return render(request, 'lessons/lesson_list.html', {'lessons': lessons})

# -----------------------------
# Single Lesson Detail
# -----------------------------
def lesson_detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    return render(request, 'lessons/lesson_detail.html', {'lesson': lesson})

# -----------------------------
# Lesson Quiz
# -----------------------------
def lesson_quiz(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    questions = QuizQuestion.objects.filter(lesson=lesson)
    
    if request.method == 'POST':
        # handle quiz submission logic
        # calculate score, save results, redirect to progress
        return redirect('lessons:lesson_progress', lesson_id=lesson.id)
    
    return render(request, 'lessons/lesson_quiz.html', {'lesson': lesson, 'quiz_questions': questions})

# -----------------------------
# Lesson Progress
# -----------------------------
def lesson_progress(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    progress = LessonProgress.objects.filter(lesson=lesson, user=request.user)
    return render(request, 'lessons/lesson_progress.html', {'lesson': lesson, 'progress': progress})

# -----------------------------
# Lesson Comments
# -----------------------------
def lesson_comments(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    comments = LessonComment.objects.filter(lesson=lesson).order_by('-created_at')
    
    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            LessonComment.objects.create(user=request.user, lesson=lesson, text=text)
            return redirect('lessons:lesson_comments', lesson_id=lesson.id)
    
    return render(request, 'lessons/lesson_comments.html', {'lesson': lesson, 'comments': comments})

# -----------------------------
# Lesson Resources
# -----------------------------
def lesson_resources(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    resources = LessonResource.objects.filter(lesson=lesson)
    return render(request, 'lessons/lesson_resources.html', {'lesson': lesson, 'resources': resources})

# -----------------------------
# Lesson Feedback
# -----------------------------
def lesson_feedback(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    
    if request.method == 'POST':
        rating = request.POST.get('rating')
        comments = request.POST.get('comments')
        LessonFeedback.objects.create(user=request.user, lesson=lesson, rating=rating, comments=comments)
        return redirect('lessons:lesson_list')
    
    return render(request, 'lessons/lesson_feedback.html', {'lesson': lesson})





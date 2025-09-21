# app/lessons/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Lesson, QuizQuestion, QuizOption, LessonProgress, LessonComment, LessonResource, LessonFeedback

# All lessons list
def lesson_list(request):
    lessons = Lesson.objects.all().order_by('created_at')
    return render(request, 'lessons/lesson_detail.html', {'lessons': lessons})

# Single lesson detail
def lesson_detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    return render(request, 'lessons/lesson_list.html', {'lesson': lesson})

# Lesson quiz
def lesson_quiz(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    questions = QuizQuestion.objects.filter(lesson=lesson)
    if request.method == 'POST':
        # Quiz submission logic (calculate score etc)
        return redirect('lesson_progress', lesson_id=lesson.id)
    return render(request, 'lessons/lesson_quiz.html', {'lesson': lesson, 'quiz_questions': questions})

# Lesson progress
def lesson_progress(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    progress = LessonProgress.objects.filter(lesson=lesson, user=request.user)
    return render(request, 'lessons/lesson_progress.html', {'lesson': lesson, 'progress': progress})

# Lesson comments
def lesson_comments(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    comments = LessonComment.objects.filter(lesson=lesson).order_by('-created_at')
    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            LessonComment.objects.create(user=request.user, lesson=lesson, text=text)
            return redirect('lesson_comments', lesson_id=lesson.id)
    return render(request, 'lessons/lesson_comments.html', {'lesson': lesson, 'comments': comments})

# Lesson resources
def lesson_resources(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    resources = LessonResource.objects.filter(lesson=lesson)
    return render(request, 'lessons/lesson_resources.html', {'lesson': lesson, 'resources': resources})

# Lesson feedback
def lesson_feedback(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    if request.method == 'POST':
        rating = request.POST.get('rating')
        comments = request.POST.get('comments')
        LessonFeedback.objects.create(user=request.user, lesson=lesson, rating=rating, comments=comments)
        return redirect('lesson_list')
    return render(request, 'lessons/lesson_feedback.html', {'lesson': lesson})

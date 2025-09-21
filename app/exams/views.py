from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Exam, ExamQuestion, ExamOption, ExamProgress, ExamFeedback

# Public view
def exam_list(request):
    exams = Exam.objects.all().order_by('date')
    return render(request, 'exams/exam_list.html', {'exams': exams})

# Public view
def exam_detail(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)
    return render(request, 'exams/exam_detail.html', {'exam': exam})

# Login required views
@login_required
def exam_quiz(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)
    questions = ExamQuestion.objects.filter(exam=exam)
    if request.method == 'POST':
        # process submission, calculate score
        score = 0
        return redirect('exams:exam_results', exam_id=exam.id)
    return render(request, 'exams/exam_quiz.html', {'exam': exam, 'questions': questions})

@login_required
def exam_results(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)
    # Example score placeholder
    score = 85
    correct = 17
    incorrect = 3
    return render(request, 'exams/exam_results.html', {
        'exam': exam,
        'score': score,
        'correct': correct,
        'incorrect': incorrect
    })

@login_required
def exam_progress(request):
    progress = ExamProgress.objects.filter(user=request.user)
    return render(request, 'exams/exam_progress.html', {'progress': progress})

@login_required
def exam_notifications(request):
    notifications = []  # Example placeholder
    return render(request, 'exams/exam_notifications.html', {'notifications': notifications})

@login_required
def exam_feedback(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)
    if request.method == 'POST':
        rating = request.POST.get('rating')
        comments = request.POST.get('comments')
        ExamFeedback.objects.create(user=request.user, exam=exam, rating=rating, comments=comments)
        return redirect('exams:exam_list')
    return render(request, 'exams/exam_feedback.html', {'exam': exam})

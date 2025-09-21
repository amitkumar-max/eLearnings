# # from django.shortcuts import render, get_object_or_404, redirect
# # from django.contrib.auth.decorators import login_required
# # from .models import Exam, ExamQuestion, ExamProgress, ExamFeedback

# # # -----------------------------
# # # Public Views
# # # -----------------------------
# # def exam_list(request):
# #     exams = Exam.objects.all().order_by('-created_at')  # show newest first
# #     return render(request, 'exams/exam_list.html', {'exams': exams})

# # def exam_detail(request, exam_id):
# #     exam = get_object_or_404(Exam, id=exam_id)
# #     return render(request, 'exams/exam_detail.html', {'exam': exam})

# # # -----------------------------
# # # Login Required Views
# # # -----------------------------
# # @login_required
# # def exam_quiz(request, exam_id):
# #     exam = get_object_or_404(Exam, id=exam_id)
# #     questions = ExamQuestion.objects.filter(exam=exam).order_by('order_index')
    
# #     if request.method == 'POST':
# #         # TODO: implement score calculation logic here
# #         score = 0
# #         return redirect('exams:exam_results', exam_id=exam.id)

# #     return render(request, 'exams/exam_quiz.html', {'exam': exam, 'questions': questions})

# # @login_required
# # def exam_results(request, exam_id):
# #     exam = get_object_or_404(Exam, id=exam_id)
# #     # Example score placeholder
# #     score = 85
# #     correct = 17
# #     incorrect = 3
# #     return render(request, 'exams/exam_results.html', {
# #         'exam': exam,
# #         'score': score,
# #         'correct': correct,
# #         'incorrect': incorrect
# #     })

# # @login_required
# # def exam_progress(request):
# #     progress = ExamProgress.objects.filter(user=request.user)
# #     return render(request, 'exams/exam_progress.html', {'progress': progress})

# # @login_required
# # def exam_notifications(request):
# #     notifications = []  # placeholder, integrate with actual notifications
# #     return render(request, 'exams/exam_notifications.html', {'notifications': notifications})

# # @login_required
# # def exam_feedback(request, exam_id):
# #     exam = get_object_or_404(Exam, id=exam_id)
# #     if request.method == 'POST':
# #         rating = request.POST.get('rating')
# #         comments = request.POST.get('comments')
# #         ExamFeedback.objects.create(user=request.user, exam=exam, rating=rating, comments=comments)
# #         return redirect('exams:exam_list')
# #     return render(request, 'exams/exam_feedback.html', {'exam': exam})



# from django.shortcuts import render, get_object_or_404
# from courses.models import Exam  # import from courses.models
# from .models import ExamProgress, ExamFeedback

# def exam_list(request):
#     exams = Exam.objects.all()
#     return render(request, "exams/exam_list.html", {"exams": exams})

# def exam_detail(request, id):
#     exam = get_object_or_404(Exam, id=id)
#     progress = ExamProgress.objects.filter(student=request.user.studentprofile, exam=exam).first()
#     return render(request, "exams/exam_detail.html", {"exam": exam, "progress": progress})



from django.shortcuts import render, get_object_or_404
from app.courses.models import Exam
from .models import ExamProgress

def exam_list(request):
    exams = Exam.objects.all()
    return render(request, "exams/exam_list.html", {"exams": exams})

def exam_detail(request, id):
    exam = get_object_or_404(Exam, id=id)
    progress = ExamProgress.objects.filter(student=request.user.studentprofile, exam=exam).first()
    return render(request, "exams/exam_detail.html", {"exam": exam, "progress": progress})

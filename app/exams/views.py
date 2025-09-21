from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Exam, Question  # Result hata diya

class ExamListView(View):
    def get(self, request):
        exams = Exam.objects.all()
        return render(request, 'exams/exam_list.html', {'exams': exams})

class ExamDetailView(View):
    def get(self, request, pk):
        exam = get_object_or_404(Exam, pk=pk)
        questions = exam.questions.all()
        return render(request, 'exams/exam_detail.html', {'exam': exam, 'questions': questions})


def exam_list(request):
    exams = Exam.objects.filter(is_published=True)
    return render(request, "exams/exam_list.html", {"exams": exams})

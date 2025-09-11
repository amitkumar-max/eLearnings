from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Lesson

class LessonDetailView(View):
    def get(self, request, pk):
        lesson = get_object_or_404(Lesson, pk=pk)
        return render(request, 'lessons/lesson_detail.html', {'lesson': lesson})







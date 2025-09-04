# from django.http import HttpResponse

# def course_list(request):
#     return HttpResponse("List of Courses")

# def course_detail(request, id):
#     return HttpResponse(f"Course Detail Page for Course ID {id}")


from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Course

class CourseListView(View):
    def get(self, request):
        courses = Course.objects.all()
        return render(request, 'courses/course_list.html', {'courses': courses})

class CourseDetailView(View):
    def get(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        return render(request, 'courses/course_detail.html', {'course': course})

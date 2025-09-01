from django.http import HttpResponse

def course_list(request):
    return HttpResponse("List of Courses")

def course_detail(request, id):
    return HttpResponse(f"Course Detail Page for Course ID {id}")

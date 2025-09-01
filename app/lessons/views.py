from django.http import HttpResponse

def lesson_list(request):
    return HttpResponse("List of Lessons")

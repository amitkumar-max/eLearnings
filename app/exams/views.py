from django.http import HttpResponse

def exam_list(request):
    return HttpResponse("List of Exams")

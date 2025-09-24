

from django.db import models
from django.utils import timezone
from app.courses.models import TimeStampedModel  # <- important
from app.students.models import StudentProfile
from django.db import models
from django.utils import timezone  # ensure ye top me hai



from django.db import models
from django.conf import settings
from django.utils import timezone
from ..courses.models import Exam



class ExamProgress(models.Model):
    student = models.ForeignKey('students.StudentProfile', on_delete=models.CASCADE)
    exam = models.ForeignKey('courses.Exam', on_delete=models.CASCADE)
    score = models.FloatField(default=0)
    completed = models.BooleanField(default=False)
    started_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.student.user.full_name} - {self.exam.title}"


class Exam(TimeStampedModel):
    course = models.ForeignKey(
        'courses.Course',
        on_delete=models.CASCADE,
        related_name="exams_from_external",  # unique name
    )
    title = models.CharField(max_length=255)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.course.title} - {self.title}"

    
    
    
    
# # from django.db import models
# # from django.utils.text import slugify
# # from django.conf import settings
# # from app.courses.models import Course, Exam   # ✅ import real Course + Exam

# # # ---------- Base ----------
# # class TimeStampedModel(models.Model):
# #     created_at = models.DateTimeField(auto_now_add=True)
# #     updated_at = models.DateTimeField(auto_now=True)

# #     class Meta:
# #         abstract = True

# # # ---------- Questions ----------
# # class ExamQuestion(TimeStampedModel):
# #     QUESTION_TYPE = [
# #         ("single", "Single Choice"),
# #         ("multiple", "Multiple Choice"),
# #         ("text", "Text"),
# #         ("boolean", "True/False"),
# #     ]
# #     exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name="questions")
# #     text = models.TextField()
# #     question_type = models.CharField(max_length=20, choices=QUESTION_TYPE, default="single")
# #     options = models.JSONField(default=list, blank=True)
# #     correct = models.JSONField(default=None, blank=True, null=True)
# #     marks = models.PositiveIntegerField(default=1)
# #     order_index = models.PositiveIntegerField(default=1)

# #     class Meta:
# #         ordering = ["exam", "order_index"]

# #     def __str__(self):
# #         return f"Q{self.order_index}: {self.text[:60]}..."

# # class ExamOption(models.Model):
# #     question = models.ForeignKey(ExamQuestion, on_delete=models.CASCADE, related_name="exam_options")
# #     option_text = models.CharField(max_length=200)
# #     is_correct = models.BooleanField(default=False)

# #     def __str__(self):
# #         return self.option_text

# # # ---------- Progress & Feedback ----------
# # class ExamProgress(models.Model):
# #     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="exam_progress_records")
# #     exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name="exam_progress_records_for_exam")
# #     completed = models.BooleanField(default=False)
# #     score = models.DecimalField(max_digits=6, decimal_places=2, default=0)

# # class ExamFeedback(TimeStampedModel):
# #     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
# #     exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
# #     rating = models.PositiveIntegerField(default=0)
# #     comments = models.TextField(blank=True)


# # exams/models.py
# # 🚫 Empty (Exam already exists inside courses/models.py)


# from django.db import models
# from django.conf import settings

# # Use string references to avoid circular import
# # Example: track student's exam progress
# class ExamProgress(models.Model):
#     student = models.ForeignKey('students.StudentProfile', on_delete=models.CASCADE)
#     exam = models.ForeignKey('courses.Exam', on_delete=models.CASCADE)
#     score = models.FloatField(default=0)
#     completed = models.BooleanField(default=False)
#     started_at = models.DateTimeField(auto_now_add=True)
#     finished_at = models.DateTimeField(null=True, blank=True)

#     def __str__(self):
#         return f"{self.student.user.full_name} - {self.exam.title}"


# class ExamFeedback(models.Model):
#     student = models.ForeignKey('students.StudentProfile', on_delete=models.CASCADE)
#     exam = models.ForeignKey('courses.Exam', on_delete=models.CASCADE)
#     feedback = models.TextField()
#     rating = models.IntegerField(default=0)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.student.user.full_name} → {self.exam.title} Feedback"



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

    
    
    
    
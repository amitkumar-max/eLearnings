# from django.db import models
# from django.conf import settings
# from app.lessons.models import Lesson, TimeStampedModel

# class Result(TimeStampedModel):
#     """
#     Tracks the result of a user for a specific lesson.
#     """
#     user = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#         related_name="results",
#         help_text="The user who attempted the lesson"
#     )
#     lesson = models.ForeignKey(
#         Lesson,
#         on_delete=models.CASCADE,
#         related_name="results",
#         help_text="The lesson associated with this result"
#     )
#     score = models.DecimalField(
#         max_digits=5,
#         decimal_places=2,
#         default=0,
#         help_text="Score obtained in this lesson"
#     )
#     completed = models.BooleanField(
#         default=False,
#         help_text="Whether the lesson has been completed"
#     )

#     class Meta:
#         unique_together = ("user", "lesson")
#         ordering = ["-id"]  # Most recent results first
#         verbose_name = "Lesson Result"
#         verbose_name_plural = "Lesson Results"

#     def __str__(self):
#         return f"{self.user.username} • {self.lesson.title} • {self.score}"

#     def mark_completed(self, score=None):
#         if score is not None:
#             self.score = score
#         self.completed = True
#         self.save()

#     @property
#     def is_passed(self):
#         PASS_THRESHOLD = 40
#         return self.score >= PASS_THRESHOLD


# class LessonProgress(models.Model):
#     student = models.ForeignKey(
#         'students.StudentProfile',
#         on_delete=models.CASCADE,
#         related_name="lesson_progress"
#     )
#     lesson = models.ForeignKey(
#         'courses.Lesson',
#         on_delete=models.CASCADE,
#         related_name="progress_records"
#     )



from django.db import models
from django.conf import settings

# Correct imports
from app.lessons.models import Lesson  # Lesson from lessons app
from app.courses.models import TimeStampedModel  # TimeStampedModel from courses app

class Result(TimeStampedModel):
    """
    Tracks the result of a user for a specific lesson.
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="results",
        help_text="The user who attempted the lesson"
    )
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        related_name="results",
        help_text="The lesson associated with this result"
    )
    score = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0,
        help_text="Score obtained in this lesson"
    )
    completed = models.BooleanField(
        default=False,
        help_text="Whether the lesson has been completed"
    )

    class Meta:
        unique_together = ("user", "lesson")
        ordering = ["-id"]
        verbose_name = "Lesson Result"
        verbose_name_plural = "Lesson Results"

    def __str__(self):
        return f"{self.user.username} • {self.lesson.title} • {self.score}"

    def mark_completed(self, score=None):
        if score is not None:
            self.score = score
        self.completed = True
        self.save()

    @property
    def is_passed(self):
        PASS_THRESHOLD = 40
        return self.score >= PASS_THRESHOLD


class LessonProgress(models.Model):
    student = models.ForeignKey(
        'students.StudentProfile',
        on_delete=models.CASCADE,
        related_name="lesson_progress"
    )
    lesson = models.ForeignKey(
        Lesson,  # Correct reference to lessons.Lesson
        on_delete=models.CASCADE,
        related_name="progress_records"
    )
    progress = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)

    class Meta:
        unique_together = ("student", "lesson")
        verbose_name = "Lesson Progress"
        verbose_name_plural = "Lesson Progress Records"

    def __str__(self):
        return f"{self.student.user.username} • {self.lesson.title} • {self.progress}%"

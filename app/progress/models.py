from django.db import models
from django.conf import settings
from lessons.models import Lesson, TimeStampedModel

class Result(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="results")
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="results")
    score = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    completed = models.BooleanField(default=False)

    class Meta:
        unique_together = ("user", "lesson")

    def __str__(self):
        return f"{self.user} • {self.lesson.title} • {self.score}"

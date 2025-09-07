from django.db import models
from django.utils.text import slugify
# from courses.models import Course, TimeStampedModel, PublishableModel
from courses.models import Course, TimeStampedModel, PublishableModel


class Exam(TimeStampedModel, PublishableModel):
    EXAM_TYPE = [
        ("practice", "Practice"),
        ("graded", "Graded"),
        ("final", "Final"),
    ]
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="exams")
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, blank=True)
    exam_type = models.CharField(max_length=20, choices=EXAM_TYPE, default="practice")
    duration_minutes = models.PositiveIntegerField(default=30)
    total_marks = models.PositiveIntegerField(default=100)
    pass_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=40.00)

    class Meta:
        ordering = ["course", "-created_at"]

    def __str__(self):
        return f"{self.course.title} • {self.title}"

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title)
            slug = base
            i = 1
            while Exam.objects.filter(course=self.course, slug=slug).exclude(pk=self.pk).exists():
                i += 1
                slug = f"{base}-{i}"
            self.slug = slug
        super().save(*args, **kwargs)


class Question(TimeStampedModel):
    QUESTION_TYPE = [
        ("single", "Single Choice"),
        ("multiple", "Multiple Choice"),
        ("text", "Text"),
        ("boolean", "True/False"),
    ]
    
    
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name="questions")
    text = models.TextField()
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPE, default="single")
    options = models.JSONField(default=list, blank=True)
    correct = models.JSONField(default=None, blank=True, null=True)
    marks = models.PositiveIntegerField(default=1)
    order_index = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ["exam", "order_index"]

    def __str__(self):
        return f"Q{self.order_index}: {self.text[:60]}..."

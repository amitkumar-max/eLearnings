# lessons/models.py
from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model

from app.courses.models import Course, TimeStampedModel, PublishableModel

User = get_user_model()

class Lesson(TimeStampedModel, PublishableModel):
    course = models.ForeignKey(
    Course,
    on_delete=models.CASCADE,
    related_name="lessons_in_lessons_app", )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, blank=True)
    order_index = models.PositiveIntegerField(default=1, db_index=True)
    content = models.TextField(blank=True)
    video_url = models.URLField(blank=True)
    resources = models.JSONField(default=list, blank=True)

    class Meta:
        ordering = ["course", "order_index"]
        unique_together = [("course", "slug")]

    def __str__(self):
        return f"{self.course.title} • {self.title}"

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title)
            slug = base
            i = 1
            while Lesson.objects.filter(course=self.course, slug=slug).exclude(pk=self.pk).exists():
                i += 1
                slug = f"{base}-{i}"
            self.slug = slug
        super().save(*args, **kwargs)


class QuizQuestion(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="quiz_questions")
    question_text = models.TextField()

    def __str__(self):
        return self.question_text[:50]


class QuizOption(models.Model):
    question = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE, related_name="options")
    option_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.option_text[:50]


class LessonProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    class Meta:
        unique_together = [('user', 'lesson')]


class LessonComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class LessonResource(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    file = models.FileField(upload_to='lesson_resources/', blank=True)


class LessonFeedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    feedback = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

# lessons/models.py
from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django.utils import timezone

from app.courses.models import Course, TimeStampedModel

User = get_user_model()


class Lesson(models.Model):
    # Link to Course model (avoid circular imports with string reference)
    course = models.ForeignKey(
        "courses.Course",
        on_delete=models.CASCADE,
        related_name="lessons_in_lessons_app",
    )

    # Lesson basic info
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    content_file = models.FileField(upload_to='lessons/content/', blank=True, null=True)
    # Videos (optional)
    video = models.FileField(upload_to="course_videos/", blank=True, null=True)  # uploaded file
    video_url = models.URLField(blank=True, null=True)  # external video link (YouTube/Vimeo)

    # Ordering and resources
    order_index = models.PositiveIntegerField(default=1, db_index=True)
    resources = models.JSONField(default=dict, blank=True)  # e.g., {"pdf": "link", "external": "link"}

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)  # set only on creation
    updated_at = models.DateTimeField(auto_now=True)      # updated on every save

    class Meta:
        ordering = ["course", "order_index"]
        unique_together = [("course", "slug")]
        indexes = [
            models.Index(fields=["course", "slug"]),
            models.Index(fields=["course", "order_index"]),
        ]

    def __str__(self):
        return f"{self.course.title} • {self.title}"

    def save(self, *args, **kwargs):
        # Auto-generate slug if not provided
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

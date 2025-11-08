

# app/lessons/models.py
from django.db import models
from django.utils.text import slugify
from django.conf import settings


class Lesson(models.Model):
    course = models.ForeignKey(
        'courses.Course',  # string reference to avoid circular import
        on_delete=models.CASCADE,
        related_name="lessons"
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True, null=False)
    content_file = models.FileField(upload_to='lessons/content/', blank=True, null=True)
    content_text = models.TextField(blank=True, null=True, default="")  # DB content from txt files
    content_path = models.CharField(max_length=300, blank=True, null=True)  # optional for txt path
    order_index = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["course", "order_index"]
        unique_together = [("course", "slug")]

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            i = 1
            while Lesson.objects.filter(course=self.course, slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{i}"
                i += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.course.title} • {self.title}"


class LessonProgress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course_slug = models.CharField(max_length=200, default="unknown")
    lesson_filename = models.CharField(max_length=200)
    progress = models.IntegerField(default=0)
    # completed = models.BooleanField(default=False)
    completed_lessons = models.ManyToManyField('lessons.Lesson', blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.course_slug} - {self.lesson_filename}"
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
class LessonComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
class LessonResource(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    file = models.FileField(upload_to='lesson_resources/', blank=True)
class LessonFeedback(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    feedback = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)




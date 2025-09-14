# app/courses/models.py
from django.db import models

# Base abstract models
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class PublishableModel(models.Model):
    is_published = models.BooleanField(default=False)
    published_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True

# Course model
class Course(TimeStampedModel, PublishableModel):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

# Lesson model
class Lesson(TimeStampedModel, PublishableModel):
    course = models.ForeignKey(Course, related_name='lessons', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, blank=True)
    content = models.TextField(blank=True)
    order_index = models.PositiveIntegerField(default=1, db_index=True)
    video_url = models.URLField(blank=True)
    resources = models.JSONField(default=list, blank=True)

    class Meta:
        ordering = ["course", "order_index"]
        unique_together = [("course", "slug")]

    def __str__(self):
        return f"{self.course.title} • {self.title}"

    def save(self, *args, **kwargs):
        # Auto-generate slug if blank
        if not self.slug:
            base = slugify(self.title)
            slug = base
            i = 1
            while Lesson.objects.filter(course=self.course, slug=slug).exclude(pk=self.pk).exists():
                i += 1
                slug = f"{base}-{i}"
            self.slug = slug
        super().save(*args, **kwargs)

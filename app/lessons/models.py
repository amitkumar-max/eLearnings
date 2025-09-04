from django.db import models
from django.utils.text import slugify
from courses.models import Course, TimeStampedModel, PublishableModel

class Lesson(TimeStampedModel, PublishableModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="lessons")
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

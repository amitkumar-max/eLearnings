# from django.db import models
# from django.conf import settings
# from django.utils.text import slugify
# from django.core.validators import MinValueValidator

# class TimeStampedModel(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True, db_index=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         abstract = True

# class PublishableModel(models.Model):
#     is_published = models.BooleanField(default=False, db_index=True)

#     class Meta:
#         abstract = True

# class Course(TimeStampedModel, PublishableModel):
#     title = models.CharField(max_length=200, unique=True)
#     slug = models.SlugField(max_length=220, unique=True, blank=True)
#     short_description = models.CharField(max_length=280, blank=True)
#     description = models.TextField(blank=True)
#     price = models.DecimalField(max_digits=10, decimal_places=2, default=0, validators=[MinValueValidator(0)])
#     language = models.CharField(max_length=40, default="en")
#     thumbnail = models.ImageField(upload_to="course_thumbs/", blank=True, null=True)
#     instructor = models.ForeignKey(
#         settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="courses_taught"
#     )
#     level = models.CharField(
#         max_length=20,
#         choices=[("beginner", "Beginner"), ("intermediate", "Intermediate"), ("advanced", "Advanced")],
#         default="beginner",
#     )
#     tags = models.JSONField(default=list, blank=True)

#     class Meta:
#         ordering = ["-created_at"]

#     def __str__(self):
#         return self.title

#     def save(self, *args, **kwargs):
#         if not self.slug:
#             base = slugify(self.title)
#             slug = base
#             i = 1
#             while Course.objects.filter(slug=slug).exclude(pk=self.pk).exists():
#                 i += 1
#                 slug = f"{base}-{i}"
#             self.slug = slug
#         super().save(*args, **kwargs)


from django.db import models

# Course model
class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# Lesson model
class Lesson(models.Model):
    course = models.ForeignKey(Course, related_name='lessons', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    order = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f"{self.course.title} - {self.title}"


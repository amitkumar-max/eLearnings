# from django.db import models
# from django.utils import timezone
# from django.utils.text import slugify
# from django.contrib.auth.models import User
# from django.conf import settings

# # app/courses/models.py
# import os
# from django.templatetags.static import static
# # Abstract Timestamp model
# class TimeStampedModel(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         abstract = True
# class Category(models.Model):
#     name = models.CharField(max_length=100)
#     slug = models.SlugField(unique=True)
#     description = models.TextField(blank=True, null=True)

#     def __str__(self):
#         return self.name
# class Course(TimeStampedModel):
#     title = models.CharField(max_length=200)
#     description = models.TextField()
#     image = models.ImageField(upload_to='courses/', blank=True, null=True)
#     slug = models.SlugField(unique=True, blank=True, null=True)  # For course_detail URL
#     is_published = models.BooleanField(default=False)  # For filtering live courses
#     description = models.TextField(blank=True, null=True)  # ✅ NEW FIELD
#     teacher = models.ForeignKey(
#     'teachers.TeacherProfile',
#     on_delete=models.CASCADE,
#     related_name="courses_taught",
#     null=True,
#     blank=True
#     )

#     def __str__(self):
#         return f"Course {self.id} by {self.teacher}"  # ORM-friendly
# # ✅ Extra: Like & Save Feature
# class CourseInteraction(models.Model):
#     user = models.ForeignKey(
#         settings.AUTH_USER_MODEL,  # ✅ use this instead of User
#         on_delete=models.CASCADE
#     )
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     liked = models.BooleanField(default=False)
#     saved = models.BooleanField(default=False)
#     completed_lessons = models.ManyToManyField('Lesson', blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.user} - {self.course}"
# class Lesson(TimeStampedModel):
#     course = models.ForeignKey(
#         Course,
#         on_delete=models.CASCADE,
#         related_name="lessons_for_course"
#     )
#     title = models.CharField(max_length=255)
#     content = models.TextField()

#     def __str__(self):
#         return f"{self.course.title} - {self.title}"

#     # ✅ Add this method
#     def get_image_url(self):
#         # Static images folder
#         base = 'images/'
#         for ext in ['.jpg', '.jpeg', '.webp']:
#             path = f"{base}{self.title|slugify}{ext}"
#             try:
#                 # Check if static file exists using Django staticfiles finder
#                 from django.contrib.staticfiles import finders
#                 if finders.find(path):
#                     return f"/static/{path}"
#             except:
#                 continue
#         # Default image
#         return "/static/images/default.jpg"
# class Exam(TimeStampedModel):
#     course = models.ForeignKey(
#         Course,
#         on_delete=models.CASCADE,
#         related_name="exams_for_course"
#     )
#     title = models.CharField(max_length=255)
#     date = models.DateField(default=timezone.now)

#     def __str__(self):
#         return f"{self.course.title} - {self.title}"
# class CourseAssignment(TimeStampedModel):
#     course = models.ForeignKey(
#         Course,
#         on_delete=models.CASCADE,
#         related_name="assignments_for_course"
#     )
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     due_date = models.DateField(default=timezone.now)

#     def __str__(self):
#         return f"{self.course.title} - {self.title}"
# class Enrollment(TimeStampedModel):
#     student = models.ForeignKey(
#         'students.StudentProfile',
#         on_delete=models.CASCADE,
#         related_name="enrollments"
#     )
#     course = models.ForeignKey(
#         Course,
#         on_delete=models.CASCADE,
#         related_name="enrollments"
#     )
#     date_enrolled = models.DateField(auto_now_add=True)

#     class Meta:
#         unique_together = ("student", "course")

#     def __str__(self):
#         return f"{self.student.user.full_name} → {self.course.title}"





from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.conf import settings
from django.contrib.staticfiles import finders

from app.teachers.models import TeacherProfile
from app.lessons.models import Lesson
from app.students.models import StudentProfile

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Course(TimeStampedModel):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='courses/', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    is_published = models.BooleanField(default=False)
    teacher = models.ForeignKey(
        TeacherProfile,
        on_delete=models.SET_NULL,
        related_name="courses_taught",
        null=True,
        blank=True
    )

    class Meta:
        ordering = ['title']

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            # Ensure unique slug
            while Course.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} by {self.teacher}"

    def get_image_url(self):
        base = 'images/'
        for ext in ['.jpg', '.jpeg', '.webp']:
            path = f"{base}{slugify(self.title)}{ext}"
            if finders.find(path):
                return f"/static/{path}"
        return "/static/images/default.jpg"





class CourseInteraction(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    liked = models.BooleanField(default=False)
    saved = models.BooleanField(default=False)
    completed_lessons = models.ManyToManyField(Lesson, blank=True)

    def __str__(self):
        return f"{self.user} - {self.course}"

class Exam(TimeStampedModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="exams_for_course")
    title = models.CharField(max_length=255)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.course.title} - {self.title}"

class CourseAssignment(TimeStampedModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="assignments_for_course")
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.course.title} - {self.title}"

class Enrollment(TimeStampedModel):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name="enrollments")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="enrollments")
    date_enrolled = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ("student", "course")

    def __str__(self):
        return f"{self.student.user.full_name} → {self.course.title}"



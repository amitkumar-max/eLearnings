from django.db import models
from django.utils import timezone
from django.utils.text import slugify
# app/courses/models.py
import os
from django.templatetags.static import static
# Abstract Timestamp model
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Course(TimeStampedModel):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='courses/', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)  # For course_detail URL
    is_published = models.BooleanField(default=False)  # For filtering live courses
    teacher = models.ForeignKey(
    'teachers.TeacherProfile',
    on_delete=models.CASCADE,
    related_name="courses_taught",
    null=True,
    blank=True
    )

    def __str__(self):
        return f"Course {self.id} by {self.teacher}"  # ORM-friendly




class Lesson(TimeStampedModel):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="lessons_for_course"
    )
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return f"{self.course.title} - {self.title}"

    # ✅ Add this method
    def get_image_url(self):
        # Static images folder
        base = 'images/'
        for ext in ['.jpg', '.jpeg', '.webp']:
            path = f"{base}{self.title|slugify}{ext}"
            try:
                # Check if static file exists using Django staticfiles finder
                from django.contrib.staticfiles import finders
                if finders.find(path):
                    return f"/static/{path}"
            except:
                continue
        # Default image
        return "/static/images/default.jpg"


class Exam(TimeStampedModel):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="exams_for_course"
    )
    title = models.CharField(max_length=255)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.course.title} - {self.title}"


class CourseAssignment(TimeStampedModel):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="assignments_for_course"
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.course.title} - {self.title}"


class Enrollment(TimeStampedModel):
    student = models.ForeignKey(
        'students.StudentProfile',
        on_delete=models.CASCADE,
        related_name="enrollments"
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="enrollments"
    )
    date_enrolled = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ("student", "course")

    def __str__(self):
        return f"{self.student.user.full_name} → {self.course.title}"

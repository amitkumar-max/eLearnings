from django.db import models
from django.utils import timezone
from django.utils.text import slugify

# Abstract Timestamp model
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Course(TimeStampedModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_published = models.BooleanField(default=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    teacher = models.ForeignKey(
        'teachers.TeacherProfile',
        on_delete=models.CASCADE,
        related_name="courses_taught",
        null=True,
        blank=True
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            # Ensure unique slug even for existing rows
            while Course.objects.filter(slug=slug).exclude(id=self.id).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


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

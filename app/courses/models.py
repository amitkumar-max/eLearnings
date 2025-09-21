# from django.db import models       # ✅ mandatory
# from django.conf import settings
# from django.utils import timezone   # ✅ for default date/time
# # Abstract Timestamp model
# class TimeStampedModel(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         abstract = True
# class Course(TimeStampedModel):
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     teacher = models.ForeignKey(
#         'teachers.TeacherProfile',
#         on_delete=models.CASCADE,
#         related_name="courses",
#         null=True,       # existing rows ke liye allow null
#         blank=True
#     )

#     def __str__(self):
#         return self.title

# class Lesson(TimeStampedModel):
#     course = models.ForeignKey(
#         'courses.Course',
#         on_delete=models.CASCADE,
#         related_name="lessons"
#     )
#     title = models.CharField(max_length=255)
#     content = models.TextField()

#     def __str__(self):
#         return f"{self.course.title} - {self.title}"

# class Exam(TimeStampedModel):
#     course = models.ForeignKey(
#         'courses.Course',
#         on_delete=models.CASCADE,
#         related_name="course_exams",  # changed from 'exams' to unique name
#     )
#     title = models.CharField(max_length=255)
#     date = models.DateField(default=timezone.now)

#     def __str__(self):
#         return f"{self.course.title} - {self.title}"


# class CourseAssignment(TimeStampedModel):
#     course = models.ForeignKey(
#         'courses.Course',
#         on_delete=models.CASCADE,
#         related_name="assignments"
#     )
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     due_date = models.DateField(null=True, blank=True)  # optional to avoid prompt

#     def __str__(self):
#         return f"{self.course.title} - {self.title}"

# class Enrollment(TimeStampedModel):
#     student = models.ForeignKey(
#         'students.StudentProfile',
#         on_delete=models.CASCADE,
#         related_name="enrollments"
#     )
#     course = models.ForeignKey(
#         'courses.Course',
#         on_delete=models.CASCADE,
#         related_name="enrollments"
#     )
#     date_enrolled = models.DateField(auto_now_add=True)

#     class Meta:
#         unique_together = ("student", "course")

#     def __str__(self):
#         return f"{self.student.user.full_name} → {self.course.title}"




from django.db import models
from django.conf import settings
from django.utils import timezone

# Abstract Timestamp model
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Course(TimeStampedModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    
    # Teacher field
    teacher = models.ForeignKey(
        'teachers.TeacherProfile',
        on_delete=models.CASCADE,
        related_name="courses_taught",
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title

class Lesson(TimeStampedModel):
    course = models.ForeignKey(
        'courses.Course',
        on_delete=models.CASCADE,
        related_name="lessons_for_course"
    )
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return f"{self.course.title} - {self.title}"

class Exam(TimeStampedModel):
    course = models.ForeignKey(
        'courses.Course',
        on_delete=models.CASCADE,
        related_name="exams_for_course"
    )
    title = models.CharField(max_length=255)
    date = models.DateField(default=timezone.now)  # ← permanent default

    def __str__(self):
        return f"{self.course.title} - {self.title}"

class CourseAssignment(TimeStampedModel):
    course = models.ForeignKey(
        'courses.Course',
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
        'courses.Course',
        on_delete=models.CASCADE,
        related_name="enrollments"
    )
    date_enrolled = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ("student", "course")

    def __str__(self):
        return f"{self.student.user.full_name} → {self.course.title}"




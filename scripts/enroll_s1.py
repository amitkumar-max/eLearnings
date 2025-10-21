# enroll_s1.py
from django.contrib.auth import get_user_model
from app.students.models import StudentProfile, Enrollment
from app.courses.models import Course, Lesson

User = get_user_model()
user = User.objects.get(email="s1@gmail.com")

student, _ = StudentProfile.objects.get_or_create(
    user=user,
    defaults={'assignments_submitted': {}}
)

all_courses = Course.objects.all()

for course in all_courses:
    enrollment, created = Enrollment.objects.get_or_create(student=student, course=course)
    if created:
        print(f"✅ Enrolled {user.email} -> {course.title}")
    else:
        print(f"ℹ️ Already enrolled in {course.title}")

    if hasattr(enrollment, 'lessons'):
        # 🔹 Case-insensitive filter fix
        lessons = Lesson.objects.filter(course__slug__iexact=course.slug)
        enrollment.lessons.set(lessons)
        enrollment.save()
        print(f"   📚 {lessons.count()} lessons attached to {course.title}")

print("🎉 All courses processed successfully!")

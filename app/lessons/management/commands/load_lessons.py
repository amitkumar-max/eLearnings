import os
from django.core.management.base import BaseCommand
from app.courses.models import Course
from app.lessons.models import Lesson

class Command(BaseCommand):
    help = "Load lessons from app/lessons/content into DB"

    def handle(self, *args, **kwargs):
        base_path = "app/lessons/content"

        for folder in os.listdir(base_path):
            course_slug = folder.strip()
            course_path = os.path.join(base_path, folder)

            if not os.path.isdir(course_path):
                continue

            try:
                course = Course.objects.get(slug=course_slug)
            except Course.DoesNotExist:
                self.stdout.write(f"❌ Course not found for folder: {course_slug}")
                continue

            self.stdout.write(f"\n📘 Course found: {course.title}")

            for idx, file_name in enumerate(sorted(os.listdir(course_path))):
                if not file_name.endswith(".txt"):
                    continue

                lesson_title = os.path.splitext(file_name)[0].replace("-", " ").title()
                lesson_path = os.path.join(course_path, file_name)

                with open(lesson_path, "r", encoding="utf-8") as f:
                    content = f.read()

                lesson, created = Lesson.objects.get_or_create(
                    course=course,
                    order_index=idx + 1,
                    defaults={"title": lesson_title, "content_text": content},
                )

                if created:
                    self.stdout.write(f"✅ Created: {lesson_title}")
                else:
                    self.stdout.write(f"⚠️ Already exists: {lesson_title}")

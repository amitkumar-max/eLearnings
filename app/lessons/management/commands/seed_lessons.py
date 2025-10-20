import os
from django.core.management.base import BaseCommand
from app.courses.models import Course
from app.lessons.models import Lesson
from django.utils.text import slugify

CONTENT_DIR = 'lesson/content/'  # adjust if your folder path is different

class Command(BaseCommand):
    help = "Seed lessons from lesson/content folder into DB"

    def handle(self, *args, **kwargs):
        subjects = os.listdir(CONTENT_DIR)
        for subject in subjects:
            subject_path = os.path.join(CONTENT_DIR, subject)
            if not os.path.isdir(subject_path):
                continue

            # Get or create Course
            course, created = Course.objects.get_or_create(
                title=subject.upper(),  # e.g., "HTML"
                slug=slugify(subject)
            )

            # Loop over lesson files
            files = sorted(os.listdir(subject_path))
            order_index = 1
            for filename in files:
                if not filename.endswith('.txt'):
                    continue
                lesson_type = os.path.splitext(filename)[0]  # intro, content, examples
                file_path = os.path.join(subject_path, filename)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content_text = f.read()

                # Check if lesson exists
                lesson, created = Lesson.objects.get_or_create(
                    course=course,
                    type=lesson_type,
                    defaults={
                        'title': f"{subject.upper()} - {lesson_type.title()}",
                        'content_text': content_text,
                        'content_path': file_path,
                        'order_index': order_index
                    }
                )
                if not created:
                    # Update existing lesson
                    lesson.content_text = content_text
                    lesson.content_path = file_path
                    lesson.order_index = order_index
                    lesson.save()

                order_index += 1
                self.stdout.write(self.style.SUCCESS(f"Added lesson: {lesson.title}"))

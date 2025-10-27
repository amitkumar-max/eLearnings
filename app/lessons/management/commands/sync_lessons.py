import os
from django.core.management.base import BaseCommand
from app.courses.models import Course
from app.lessons.models import Lesson

BASE_PATH = 'app/lessons/content/'

class Command(BaseCommand):
    help = 'Sync lessons from content folders'

    def handle(self, *args, **kwargs):
        for course_slug in os.listdir(BASE_PATH):
            course_path = os.path.join(BASE_PATH, course_slug)
            if not os.path.isdir(course_path):
                continue

            # Get or create course
            course, _ = Course.objects.get_or_create(
                slug=course_slug,
                defaults={'title': course_slug.replace('-', ' ').title()}
            )

            # Lesson slug
            lesson_slug = f"{course_slug}-introduction"
            lesson, created = Lesson.objects.get_or_create(
                slug=lesson_slug,
                course=course,
                defaults={'title': 'Introduction'}
            )

            if not created:
                lesson.title = 'Introduction'
                lesson.save()

            self.stdout.write(f"{'Created' if created else 'Updated'} lesson: {lesson_slug}")

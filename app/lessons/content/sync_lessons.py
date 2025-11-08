# import os
# from django.core.management.base import BaseCommand
# from app.courses.models import Course
# from app.lessons.models import Lesson

# BASE_PATH = 'app/lessons/content/'

# class Command(BaseCommand):
#     help = 'Sync lessons from content folders'

#     def handle(self, *args, **kwargs):
#         for course_slug in os.listdir(BASE_PATH):
#             course_path = os.path.join(BASE_PATH, course_slug)
#             if not os.path.isdir(course_path):
#                 continue

#             # Get or create course
#             course, _ = Course.objects.get_or_create(
#                 slug=course_slug,
#                 defaults={'title': course_slug.replace('-', ' ').title()}
#             )

#             # Lesson slug
#             lesson_slug = f"{course_slug}-introduction"
#             lesson, created = Lesson.objects.get_or_create(
#                 slug=lesson_slug,
#                 course=course,
#                 defaults={'title': 'Introduction'}
#             )

#             if not created:
#                 lesson.title = 'Introduction'
#                 lesson.save()

#             self.stdout.write(f"{'Created' if created else 'Updated'} lesson: {lesson_slug}")


import os
from django.utils.text import slugify
from django.core.management.base import BaseCommand
from app.courses.models import Course
from app.lessons.models import Lesson

BASE_PATH = 'app/lessons/content/'

class Command(BaseCommand):
    help = 'Sync all HTML and TXT lessons from content folders into the database'

    def handle(self, *args, **kwargs):
        order_index = 1
        total_created, total_updated = 0, 0

        for course_slug in os.listdir(BASE_PATH):
            course_path = os.path.join(BASE_PATH, course_slug)
            if not os.path.isdir(course_path):
                continue

            # --- Fetch the matching course ---
            try:
                course = Course.objects.get(slug=slugify(course_slug))
                self.stdout.write(self.style.SUCCESS(f"\n📘 Course found: {course.title}"))
            except Course.DoesNotExist:
                self.stdout.write(self.style.WARNING(f"⚠️ Course not found for '{course_slug}', skipping"))
                continue

            # --- Iterate through each file in the course folder ---
            for file_name in sorted(os.listdir(course_path)):
                if not (file_name.endswith(".html") or file_name.endswith(".txt")):
                    continue

                file_path = os.path.join(course_path, file_name)
                with open(file_path, "r", encoding="utf-8") as f:
                    file_content = f.read()

                # Title and slug creation
                title = (
                    file_name.replace("_", " ")
                    .replace("-", " ")
                    .replace(".html", "")
                    .replace(".txt", "")
                    .title()
                )
                slug = slugify(title)

                # Create or update lesson
                lesson, created = Lesson.objects.get_or_create(
                    course=course,
                    slug=slug,
                    defaults={
                        "title": title,
                        "content_path": file_path,
                        "order_index": order_index,
                    },
                )

                # Update existing lesson content
                if file_name.endswith(".html"):
                    lesson.content_file.name = file_path.replace("app/", "")
                else:
                    lesson.content_text = file_content

                lesson.order_index = order_index
                lesson.save()

                order_index += 1
                if created:
                    total_created += 1
                    self.stdout.write(f"✅ Created: {title}")
                else:
                    total_updated += 1
                    self.stdout.write(f"🔁 Updated: {title}")

        self.stdout.write(
            self.style.SUCCESS(f"\n✨ Sync complete — {total_created} created, {total_updated} updated lessons.")
        )

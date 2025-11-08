# import os
# from django.core.management.base import BaseCommand
# from app.courses.models import Course
# from app.lessons.models import Lesson

# BASE_PATH = 'app/lessons/content/'

# class Command(BaseCommand):
#     help = 'Auto-sync all lessons (HTML preferred, fallback to TXT) from content folders into the database'

#     def handle(self, *args, **kwargs):
#         for course_slug in os.listdir(BASE_PATH):
#             course_path = os.path.join(BASE_PATH, course_slug)
#             if not os.path.isdir(course_path):
#                 continue

#             course, _ = Course.objects.get_or_create(
#                 slug=course_slug,
#                 defaults={'title': course_slug.replace('-', ' ').title()}
#             )

#             for file_name in os.listdir(course_path):
#                 if not (file_name.endswith('.html') or file_name.endswith('.txt')):
#                     continue

#                 base_name = os.path.splitext(file_name)[0]
#                 lesson_slug = f"{course_slug}-{base_name}".replace(' ', '-').lower()
#                 lesson_title = base_name.replace('_', ' ').replace('-', ' ').title()

#                 html_path = os.path.join(course_path, f"{base_name}.html")
#                 txt_path = os.path.join(course_path, f"{base_name}.txt")
#                 file_path = html_path if os.path.exists(html_path) else txt_path

#                 if not os.path.exists(file_path):
#                     self.stdout.write(f"⚠️ Skipped (no file found): {lesson_slug}")
#                     continue

#                 try:
#                     with open(file_path, 'r', encoding='utf-8') as f:
#                         content_data = f.read()
#                 except Exception as e:
#                     self.stdout.write(f"❌ Error reading {file_path}: {e}")
#                     continue

#                 # 👇 Using 'description' instead of 'content'
#                 lesson, created = Lesson.objects.get_or_create(
#                     slug=lesson_slug,
#                     course=course,
#                     defaults={
#                         'title': lesson_title,
#                         'description': content_data
#                     }
#                 )

#                 updated = False
#                 if not created:
#                     if lesson.title != lesson_title:
#                         lesson.title = lesson_title
#                         updated = True
#                     if getattr(lesson, "description", "") != content_data:
#                         lesson.description = content_data
#                         updated = True
#                     if updated:
#                         lesson.save()

#                 status = "🟢 Created" if created else ("🟡 Updated" if updated else "⚪ Skipped (No Change)")
#                 self.stdout.write(f"{status}: {lesson_slug}")

#         self.stdout.write(self.style.SUCCESS("✅ All lessons synced successfully!"))



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

        # --- Normalize slug & try matching course ---
        normalized_slug = slugify(course_slug)
        course = Course.objects.filter(slug=normalized_slug).first()

        # 🔁 If not found, try removing "-intro" or similar endings
        if not course and normalized_slug.endswith("-intro"):
            alt_slug = normalized_slug.replace("-intro", "")
            course = Course.objects.filter(slug=alt_slug).first()

        # You can even expand to handle cases like "-basics" etc.
        if not course:
            alt_slug2 = normalized_slug.replace("-basics", "")
            course = Course.objects.filter(slug=alt_slug2).first()

        # --- Continue if still not found ---
        if not course:
            self.stdout.write(self.style.WARNING(f"⚠️ Course not found for '{course_slug}', skipping"))
            continue

        self.stdout.write(self.style.SUCCESS(f"\n📘 Course found: {course.title}"))

        # --- Iterate through each file in the course folder ---
        for file_name in sorted(os.listdir(course_path)):
            if not (file_name.endswith(".html") or file_name.endswith(".txt")):
                continue

            file_path = os.path.join(course_path, file_name)
            with open(file_path, "r", encoding="utf-8") as f:
                file_content = f.read()

            # Title + slugify
            title = (
                file_name.replace("_", " ")
                .replace("-", " ")
                .replace(".html", "")
                .replace(".txt", "")
                .title()
            )
            slug = slugify(title)

            lesson, created = Lesson.objects.get_or_create(
                course=course,
                slug=slug,
                defaults={
                    "title": title,
                    "content_path": file_path,
                    "order_index": order_index,
                },
            )

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
        self.style.SUCCESS(
            f"\n✨ Sync complete — {total_created} created, {total_updated} updated lessons."
        )
    )

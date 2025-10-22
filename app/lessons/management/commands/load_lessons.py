
# # import os
# # from django.core.management.base import BaseCommand
# # from app.courses.models import Course
# # from app.lessons.models import Lesson

# # class Command(BaseCommand):
# #     help = "Load lessons from app/lessons/content into DB"

# #     def handle(self, *args, **kwargs):
# #         # Adjust this path if needed
# #         lessons_dir = os.path.join("app", "lessons", "content")

# #         for folder_name in os.listdir(lessons_dir):
# #             folder_path = os.path.join(lessons_dir, folder_name)

# #             if not os.path.isdir(folder_path):
# #                 continue

# #             # Auto-create course if it doesn't exist
# #             course, created = Course.objects.get_or_create(
# #                 slug=folder_name,
# #                 defaults={'title': folder_name.replace("-", " ").title()}
# #             )
# #             if created:
# #                 self.stdout.write(f"📘 Auto-created Course: {course.title}")

# #             # Loop through all .txt files in the folder
# #             for file_name in os.listdir(folder_path):
# #                 if not file_name.endswith(".txt"):
# #                     continue

# #                 lesson_slug = file_name.replace(".txt", "")
# #                 lesson_path = os.path.join(folder_path, file_name)

# #                 with open(lesson_path, "r", encoding="utf-8") as f:
# #                     content = f.read()

# #                 # Create lesson if it doesn't exist
# #                 lesson, l_created = Lesson.objects.get_or_create(
# #                     course=course,
# #                     slug=lesson_slug,
# #                     defaults={
# #                         'title': lesson_slug.replace("-", " ").title(),
# #                         'content_text': content  # Store content here
# #                     }
# #                 )

# #                 if l_created:
# #                     self.stdout.write(f"✅ Added Lesson: {lesson.title} for {course.title}")
# #                 else:
# #                     self.stdout.write(f"⚠️ Already exists: {lesson.title}")


# import os
# from django.core.management.base import BaseCommand
# from app.courses.models import Course
# from app.lessons.models import Lesson

# class Command(BaseCommand):
#     help = "Load lessons from app/lessons/content into DB"

#     def handle(self, *args, **kwargs):
#         lessons_dir = os.path.join("app", "lessons", "content")

#         for folder_name in os.listdir(lessons_dir):
#             folder_path = os.path.join(lessons_dir, folder_name)
#             if not os.path.isdir(folder_path):
#                 continue

#             # Map folder to course title (optional: you can customize)
#             course_title = folder_name.split("-")[0].title()  # e.g., python-for-data-science -> Python
#             course, created = Course.objects.get_or_create(
#                 title=course_title,
#                 defaults={'slug': course_title.lower()}
#             )
#             if created:
#                 self.stdout.write(f"📘 Auto-created Course: {course.title}")

#             # Loop through .txt files
#             for file_name in os.listdir(folder_path):
#                 if not file_name.endswith(".txt"):
#                     continue

#                 lesson_slug = file_name.replace(".txt", "")
#                 lesson_path = os.path.join(folder_path, file_name)

#                 with open(lesson_path, "r", encoding="utf-8") as f:
#                     content = f.read()

#                 # Create lesson if not exists
#                 lesson, l_created = Lesson.objects.get_or_create(
#                     course=course,
#                     slug=lesson_slug,
#                     defaults={
#                         'title': lesson_slug.replace("-", " ").title(),
#                         'content_text': content  # update if your model field is 'content'
#                     }
#                 )

#                 if l_created:
#                     self.stdout.write(f"✅ Added Lesson: {lesson.title} for {course.title}")
#                 else:
#                     self.stdout.write(f"⚠️ Already exists: {lesson.title}")


import os
from django.core.management.base import BaseCommand
from app.courses.models import Course
from app.lessons.models import Lesson

class Command(BaseCommand):
    help = "Load lessons from app/lessons/content into DB"

    def handle(self, *args, **kwargs):
        lessons_dir = os.path.join("app", "lessons", "content")

        for folder_name in os.listdir(lessons_dir):
            folder_path = os.path.join(lessons_dir, folder_name)
            if not os.path.isdir(folder_path):
                continue

            # Define course slug (optional: you can map folders to actual courses)
            course_slug = folder_name.split("-")[0].lower()  # e.g., python-intro -> python
            course_title = course_slug.title()

            # Check if course exists
            course = Course.objects.filter(slug=course_slug).first()
            if not course:
                course = Course.objects.create(title=course_title, slug=course_slug)
                self.stdout.write(f"📘 Auto-created Course: {course.title}")

            # Loop through .txt files for lessons
            for file_name in os.listdir(folder_path):
                if not file_name.endswith(".txt"):
                    continue

                lesson_slug = file_name.replace(".txt", "").lower()
                lesson_path = os.path.join(folder_path, file_name)

                with open(lesson_path, "r", encoding="utf-8") as f:
                    content = f.read()

                # Check if lesson already exists
                lesson = Lesson.objects.filter(course=course, slug=lesson_slug).first()
                if lesson:
                    self.stdout.write(f"⚠️ Already exists: {lesson.title}")
                    continue

                # Create lesson
                lesson = Lesson.objects.create(
                    course=course,
                    slug=lesson_slug,
                    title=lesson_slug.replace("-", " ").title(),
                    content_text=content  # make sure field matches your model
                )
                self.stdout.write(f"✅ Added Lesson: {lesson.title} for {course.title}")

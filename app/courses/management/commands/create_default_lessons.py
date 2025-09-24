from django.core.management.base import BaseCommand
from app.courses.models import Course, Lesson

class Command(BaseCommand):
    help = "Auto-create intro + reading lessons for all courses without lessons"

    def handle(self, *args, **kwargs):
        for course in Course.objects.all():
            if course.lessons_in_lessons_app.exists():
                continue

            # Intro Lesson
            Lesson.objects.create(
                course=course,
                title=f"Introduction to {course.title}",
                order_index=1,
                content="Welcome! This is the intro lesson.",
                video_url="https://example.com/intro.mp4"
            )

            # Reading Lessons
            topics = ["Lesson 1: Basics", "Lesson 2: Intermediate", "Lesson 3: Advanced"]
            for i, topic in enumerate(topics, start=2):
                Lesson.objects.create(
                    course=course,
                    title=topic,
                    order_index=i,
                    content=f"This is the reading content for {topic}."
                )

        self.stdout.write(self.style.SUCCESS("✅ Lessons created successfully!"))

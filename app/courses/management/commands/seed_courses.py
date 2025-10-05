from django.core.management.base import BaseCommand
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from app.courses.models import Course
import os
import json
from django.conf import settings
from datetime import datetime

class Command(BaseCommand):
    help = "Seed demo courses with unique images, and auto-backup old ones."

    def handle(self, *args, **options):
        # ----------------------------
        # 1️⃣ Create Backup Folder
        # ----------------------------
        backup_dir = os.path.join(settings.BASE_DIR, "backups")
        os.makedirs(backup_dir, exist_ok=True)

        backup_file = os.path.join(
            backup_dir,
            f"courses_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        )

        # ----------------------------
        # 2️⃣ Backup Existing Data
        # ----------------------------
        existing_courses = list(
            Course.objects.all().values(
                "id", "title", "slug", "description", "image", "is_published"
            )
        )
        if existing_courses:
            with open(backup_file, "w", encoding="utf-8") as f:
                json.dump(existing_courses, f, indent=4, ensure_ascii=False)
            self.stdout.write(self.style.WARNING(f"💾 Backup created at: {backup_file}"))
        else:
            self.stdout.write(self.style.WARNING("⚠️ No existing courses found — skipping backup."))

        # ----------------------------
        # 3️⃣ Seeding Logic
        # ----------------------------
        instructor = get_user_model().objects.first()

        titles = [
            "JavaScript", "jQuery", "C++", "MySQL", "Node.js", "ReactJS",
            "HTML", "CSS", "Bootstrap", "Python", "Java", "PHP", "Django"
        ]
        images = [
            "crs2.jpg", "crs3.webp", "crs4.jpg", "crs5.jpg", "crs6.jpg", "crs7.webp",
            "crs8.jpg", "crs9.jpg", "crs10.jpg", "crs11.jpg", "crs12.jpg", "crs13.jpg", "crs14.jpg"
        ]

        for i, t in enumerate(titles):
            slug = slugify(t)
            Course.objects.update_or_create(
                slug=slug,
                defaults={
                    "title": t,
                    "description": f"Learn {t} with practical examples and projects.",
                    "teacher": instructor.teacherprofile if hasattr(instructor, "teacherprofile") else None,
                    "image": f"courses/{images[i]}",
                    "is_published": True,
                },
            )

        # ----------------------------
        # 4️⃣ Done Message
        # ----------------------------
        self.stdout.write(self.style.SUCCESS("✅ Courses safely updated/created with unique images!"))

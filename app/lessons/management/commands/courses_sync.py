from django.core.management.base import BaseCommand
from datetime import datetime
from app.courses.models import Course

class Command(BaseCommand):
    help = "Sync Photoshop and multimedia courses into the courses_course table."

    def handle(self, *args, **kwargs):
        COURSES = [
            ("3D Collage Effect", "photoshop-basics-3d-collage-effect", "Learn 3D collage effect in Photoshop"),
            ("Bubble Effect", "photoshop-basics-bubble-effect", "Create bubble effects using layer blending"),
            ("Cloud Face", "photoshop-basics-cloud-face", "Make a surreal cloud-face manipulation"),
            ("Dispersion Effect", "photoshop-basics-dispersion-effect", "Disintegrate your image particles"),
            ("Eye Blending Effect", "photoshop-basics-eye-blending-effect", "Glow eyes using blending modes"),
            ("Headlight Blinking Effect", "photoshop-basics-headlight-blinking-effect", "Make car headlights blink realistically"),
            ("Reflection Effect", "photoshop-basics-reflection-effect", "Add reflective surfaces & mirrors"),
            ("Slice Head", "photoshop-basics-slice-head", "Creative slice-head manipulation"),
        ]

        added, skipped = 0, 0

        for title, slug, desc in COURSES:
            if not Course.objects.filter(slug=slug).exists():
                Course.objects.create(
                    title=title,
                    slug=slug,
                    description=desc,
                    is_published=True,
                    created_at=datetime.now(),
                    updated_at=datetime.now(),
                )
                self.stdout.write(self.style.SUCCESS(f"✅ Added: {title}"))
                added += 1
            else:
                self.stdout.write(self.style.WARNING(f"⚠️ Skipped (already exists): {title}"))
                skipped += 1

        self.stdout.write("\nSummary:")
        self.stdout.write(self.style.SUCCESS(f"Added: {added}, Skipped: {skipped}"))

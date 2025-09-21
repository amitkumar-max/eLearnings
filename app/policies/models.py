from django.db import models
from django.utils.text import slugify

class Policy(models.Model):
    POLICY_TYPE = [
        ("faq", "FAQ"),
        ("refund", "Refund Policy"),
        ("privacy", "Privacy Policy"),
    ]
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, blank=True, unique=True)
    content = models.TextField()
    policy_type = models.CharField(max_length=20, choices=POLICY_TYPE, default="faq")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['policy_type', 'title']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.policy_type.upper()}: {self.title}"

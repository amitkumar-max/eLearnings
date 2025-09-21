from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class File(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='downloads/')
    size = models.FloatField(help_text="File size in MB")
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    # Optional: calculate file size automatically
    # def save(self, *args, **kwargs):
    #     if self.file:
    #         self.size = self.file.size / (1024*1024)  # Convert bytes to MB
    #     super().save(*args, **kwargs)

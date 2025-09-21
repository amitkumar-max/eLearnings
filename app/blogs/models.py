from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# --------------------------
# Blog Model
# --------------------------
class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Optional: add tags or categories
    # tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title


# --------------------------
# Comment Model
# --------------------------
class Comment(models.Model):
    blog = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.blog.title}"

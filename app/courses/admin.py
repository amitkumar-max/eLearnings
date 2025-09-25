from django.contrib import admin
from .models import Course, Category

# ✅ Category admin
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}  # slug automatically fill ho jaye name se
    list_display = ("name", "slug")            # admin me columns show honge

# ✅ Course admin
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    # list_display = ("title", "category", "is_published")
    # list_filter = ("category", "is_published")  # filter option in admin

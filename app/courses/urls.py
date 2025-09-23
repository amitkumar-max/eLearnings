from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = "courses"

urlpatterns = [
    # Course list page (main page)
    path("", views.course_list, name="course_list"),

    # Course detail page (dynamic by slug)
    path("<slug:slug>/", views.course_detail, name="course_detail"),

    # Categories page
    path("categories/", views.categories, name="categories"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path
from . import views

app_name = "courses"

urlpatterns = [
    # Course list page (main page)
    path("", views.course_list, name="course_list"),

    # Course detail page (dynamic by slug)
    path("<slug:slug>/", views.course_detail, name="course_detail"),

    # Categories page
    path("categories/", views.categories, name="categories"),
]

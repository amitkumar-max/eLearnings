# # from django.urls import path
# # from . import views

# # urlpatterns = [
# #     path('', views.course_list, name='course_list'),
# #     path('<int:id>/', views.course_detail, name='course_detail'),
# # ]
# from django.urls import path
# from .views import CourseListView, CourseDetailView

# urlpatterns = [
#     path('', CourseListView.as_view(), name='course_list'),
#     path('<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
# ]


from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('<int:course_id>/', views.course_detail, name='course_detail'),
]

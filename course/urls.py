from django.urls import path, include
from course.views import CourseView

urlpatterns = [
    path(
        "",
        CourseView.as_view(),
    )
]

from django.urls import path, include
from library.views import LibraryView

urlpatterns = [
    path(
        "",
        LibraryView.as_view(),
    )
]
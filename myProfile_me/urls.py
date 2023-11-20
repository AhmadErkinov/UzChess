from django.urls import path, include
from myProfile_me.views import My

urlpatterns = [
    path(
        "",
        LibraryView.as_view(),
    )
]
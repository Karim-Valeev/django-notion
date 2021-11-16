from django.urls import path
from django.urls import re_path
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from .views import *


router = SimpleRouter()
router.register("notes", NoteViewSet, "notes")

urlpatterns = [
    path("", test_api_view),
    *router.urls,
]

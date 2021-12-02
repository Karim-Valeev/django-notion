from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt import views as jwt_views

from .views import *

router = SimpleRouter()
router.register("notes", NoteViewSet, "notes")
# .../notes
# .../notes/id

urlpatterns = [
    path("check/", check_api_view, name="api-check"),
    path("register/", UserCreate.as_view(), name="api-register"),
    path("token/", jwt_views.TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
    *router.urls,
]

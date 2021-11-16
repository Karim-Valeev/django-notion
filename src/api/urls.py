from django.urls import path, re_path
from rest_framework.routers import SimpleRouter, DefaultRouter

from .views import *


# роутер нужен, чтобы сгенерить урлы под вью сет и самому их не прописывать соотвественно
router = SimpleRouter()
# router.register('baskets', BasketViewSet, 'baskets')

urlpatterns = [
    path("", test_api_view),
    *router.urls,
]

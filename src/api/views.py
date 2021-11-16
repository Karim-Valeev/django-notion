from api.models import Note
from api.serializers import NoteCreateSerializer
from api.serializers import NoteSerializer
from api.serializers import NoteUpdateSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import BasePermission
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

# from api.serializers import BasketSerializer, BasketCreateSerializer, BasketUpdateSerializer
# from main.models import Basket, Status


# todo поменять автора расписанного на просто айди
# todo исправить создание чтобы автора сделать не предлагал
# todo сделать нормальну. рест апи авторизацию
# todo добавить update по полям и целый правильный


@api_view(["GET"])
def test_api_view(request):
    """Method for checking api"""
    return Response({"status": "ok"})


class NoteChangeOnlyForOwnerPermission(BasePermission):
    # Todo добавь логику апи ключа
    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False
        return obj.author_id == request.user.id


#
#
# # ModelViewSet include a lot of useful mixins such as List, Generic, CRUD
class NoteViewSet(ModelViewSet):
    """Baskets"""

    permission_classes = [NoteChangeOnlyForOwnerPermission]
    serializer_class = NoteSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer: NoteSerializer):
        author = self.request.user
        # url = "https://www.django-rest-framework.org/"+self.
        serializer.save(author=author)

    def get_serializer_class(self):
        if self.action == "retrieve":
            return NoteSerializer
        if self.action == "create":
            return NoteCreateSerializer
        if self.action == "update":
            return NoteUpdateSerializer
        return NoteSerializer

    def get_queryset(self):
        user = self.request.user
        # qs = Note.objects.select_related('owner', 'status')
        qs = Note.objects.all()
        if user.is_authenticated:
            qs = qs.filter(author=user)
        return qs

    def list(self, request, *args, **kwargs):
        """Выводит список корзин"""
        return super(NoteViewSet, self).list(request, *args, **kwargs)

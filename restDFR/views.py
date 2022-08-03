from django.shortcuts import render
from django.forms import model_to_dict
from rest_framework import generics, viewsets, mixins
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
    IsAdminUser,
)
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .pagination import GameAPIListPagination
from restDFR.models import Game, Category
from restDFR.serializers import GameSerializers
from rest_framework.views import APIView
from rest_framework.response import Response


class GameAPIList(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializers
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ["title"]
    search_fields = ["title"]
    pagination_class = GameAPIListPagination


class GameAPIUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializers
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication, )
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ["title"]
    search_fields = ["title"]


class GameDetailAPIDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializers
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ["title"]
    search_fields = ["title"]


# class GameViewSet(viewsets.mixins.CreateModelMixin,
#                    mixins.RetrieveModelMixin,
#                    mixins.UpdateModelMixin,
#                    mixins.DestroyModelMixin,
#                    mixins.ListModelMixin,
#                    GenericViewSet):
#     # queryset = Game.objects.all()
#     serializer_class = GameSerializers
#
#     def get_queryset(self):
#         pk = self.kwargs.get("pk")
#         if not pk:
#             return Game.objects.all()[::3]
#
#         return Game.objects.filter(pk=pk)
#
#     @action(methods=['GET'], detail=True)
#     def category(self, request, pk=None):
#         cats = Category.objects.get(pk=pk)
#         return Response({'cats': [c.name for c in cats]})

# class GameAPIview(APIView):
#     def get(self, request):
#         game = Game.objects.all()
#         return Response({'posts': GameSerializers(game, many=True).data})
#
#     def post(self, request):
#         serializer = GameSerializers(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"errors": "Method PUT not allowed"})
#
#         try:
#             instance = Game.objects.get(pk=pk)
#
#         except:
#             return Response({"errors": "Objects does not exists"})
#
#         serializer = GameSerializers(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"errors": "Method delete not allowed"})
#         game = Game.objects.get(pk=pk)
#         game.delete()
#         return Response({"posts": "delete post " + str(pk)})


# class GameAPIview(generics.ListAPIView):
#     queryset = Game.objects.all()
#     serializer_class = GameSerializers

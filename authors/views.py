from django.shortcuts import render
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.viewsets import ModelViewSet
from rest_framework.renderers import BaseRenderer

from authors.models import Author
from authors.serializers import AuthorModelSerializer


class AuthorsViewSet(ModelViewSet):
    #renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer


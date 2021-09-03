from django.shortcuts import render
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.viewsets import ModelViewSet
from rest_framework.renderers import BaseRenderer

from mainapp.models import Book
from mainapp.serializers import BookSerializer


class BooksViewSet(ModelViewSet):

    queryset = Book.objects.all()
    serializer_class = BookSerializer

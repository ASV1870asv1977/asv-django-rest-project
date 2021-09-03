from django.db import models

from authors.models import Author


class Book(models.Model):
    name = models.CharField(max_length=32)
    authors = models.ManyToManyField(Author)


class Article(models.Model):
    name = models.CharField(max_length=32)
    author = models.ForeignKey(Author, models.PROTECT)
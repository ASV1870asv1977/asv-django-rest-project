import io

from django.core.management.base import BaseCommand
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.parsers import JSONParser

from mainapp.management.commands.python_models import Author


class Command(BaseCommand):
    def handle(self, *args, **options):

        class AuthorSerialiser(serializers.Serializer):
            name = serializers.CharField(max_length=128)
            birthday_year = serializers.IntegerField()

            def create(self, validated_data):
                return Author(**validated_data)

        author = Author('Grin', 1880)
        serializer = AuthorSerialiser(author)
        author_s = dict(serializer.data)
        print(author_s)
        print(type(serializer.data), type(author_s))

        rev_serializer = AuthorSerialiser(data=author_s)
        rev_serializer.is_valid()

        print(rev_serializer.errors)
        print('-', rev_serializer)
        print(rev_serializer.validated_data)

        author_new = rev_serializer.save()
        print('*', author_new, type(author_new))

        # -----------------------------------

        json_bytes = JSONRenderer().render(serializer.data)
        print(json_bytes)
        print(type(json_bytes))

        # -----------------------------------

        stream = io.BytesIO(json_bytes)
        parser = JSONParser()
        data = parser.parse(stream)
        print(data)
        print(type(data))

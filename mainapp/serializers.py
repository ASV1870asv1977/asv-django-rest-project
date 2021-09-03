from rest_framework.relations import StringRelatedField
from rest_framework.serializers import ModelSerializer

from authors.serializers import AuthorModelSerializer
from mainapp.models import Article, Book


class ArticleSerializer(ModelSerializer):
    author = AuthorModelSerializer()

    class Meta:
        model = Article
        fields = '__all__'


class BookSerializer(ModelSerializer):
    authors = StringRelatedField(many=True)

    class Meta:
        model = Book
        fields = '__all__'

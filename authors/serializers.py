from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer

from authors.models import Author, Biography


class AuthorModelSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BiographySerializer(ModelSerializer):
    class Meta:
        model = Biography
        fields = ['text', 'author']

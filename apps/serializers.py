from rest_framework import serializers

from apps.models import Book


class BookSerializer(serializers.ModelSerializer):
    prices = serializers.IntegerField(source='price')
    class Meta:
        model = Book
        fields = ('title', 'description', 'prices', 'image', 'category')

class BookListSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name')

    class Meta:
        model = Book
        fields = ('title', 'description', 'image', 'category', 'price')


from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from apps.filters import ProductFilter
from apps.models import Book
from apps.serializers import BookSerializer, BookListSerializer


# Create your views here.

class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filterset_class = ProductFilter
    # filter_backends = [DjangoFilterBackend]
    filterset_fields = ('category')

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BookListSerializer
        return BookSerializer

class BookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookListSerializer



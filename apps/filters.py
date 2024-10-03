import django_filters
from django_filters import FilterSet, NumberFilter

from apps.models import Book


class ProductFilter(FilterSet):
    min_price = NumberFilter(field_name="price", lookup_expr='gte')
    max_price = NumberFilter(field_name="price", lookup_expr='lte')
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]

    class Meta:
        model = Book
        fields = ['title', 'category']
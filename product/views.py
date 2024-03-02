from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
# from rest_framework.pagination import CursorPagination
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import *


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# class MyCursorPagination(CursorPagination):
#     page_size = 1
#     ordering = '-created_at'


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # pagination_class = MyCursorPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category', 'in_stock']
    search_fields = ['title', 'body']
    ordering_fields = ['price', 'created_at']



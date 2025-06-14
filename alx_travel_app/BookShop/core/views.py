# core/views.py
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import CategorySerializer, ProductSerializer
from .models import Category, Product


class CategoryListCreateView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Only return categories for the current user
        return Category.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically associate the user with the category
        serializer.save(user=self.request.user)


class ProductListCreateView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Only return products for the current user
        return Product.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically associate the user with the product
        serializer.save(user=self.request.user)

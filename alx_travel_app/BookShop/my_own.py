from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .serializers import CategorySerializer, ProductSerializer
from .models import Category, Product


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def categories_list(request):
    """
    List or create categories belonging to the current user only.
    """
    if request.method == "GET":
        categories = Category.objects.filter(user=request.user)
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "POST":
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(
            {"detail": "Error saving the category", "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )



@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def products_list(request):
    """
    List all products belonging to the authenticated user
    or create a new one tied to that user.
    """
    if request.method == "GET":
        products = Product.objects.filter(user=request.user)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            # Tie the product to the authenticated user
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(
            {"detail": "Error saving the product", "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )

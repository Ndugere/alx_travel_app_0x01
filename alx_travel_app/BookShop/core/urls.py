from django.urls import path
from .views import CategoryListCreateView, ProductListCreateView

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='categories'),
    path('products/', ProductListCreateView.as_view(), name='products'),
]

from django.shortcuts import render
from rest_framework.viewsets import mixins, GenericViewSet
from .serializers import ProductSerializer
from .models import Product

class ProductViewset(mixins.ListModelMixin, GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


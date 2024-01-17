from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from shop.serializers import ProductSerializer
from shop.models import Product


class ProductView_get(APIView):
    def get(self, request, **kwargs):
        _id = kwargs.get("id")
        product = get_object_or_404(Product, id=_id)
        serializer = ProductSerializer(product, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

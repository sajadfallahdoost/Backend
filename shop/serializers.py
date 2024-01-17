from rest_framework import serializers
from shop.models import Product, ProductImage, Comment


class ProductSerializer(serializers.ModelSerializer):
    class meta:
        Model = Product
        field = "__all__"


class ProductImageSerializer(serializers.ModelSerializer):
    class meta:
        Model = ProductImage
        field = "__all__"


class commentSerializer(serializers.ModelSerializer):
    class meta:
        Model = Comment
        field = "__all__"

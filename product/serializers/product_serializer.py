from rest_framework import serializers

from product.models.product import Product
from product.serializers import CategorySerializer



class ProductSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(required=True, many=True)

    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'description',
            'price',
            'active',
            'categories',
        ]
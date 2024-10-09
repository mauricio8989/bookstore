from rest_framework import serializers

from product.models.category import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "title",
            "description",
            "slug",
            "active",
        ]
        extra_kwargs = {"slug": {"required": False}}

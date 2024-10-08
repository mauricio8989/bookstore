# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# from rest_framework.permissions import IsAuthenticated

from rest_framework.viewsets import ModelViewSet
from product.models import Category
from product.serializers import CategorySerializer


class CategoryViewSet(ModelViewSet):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all().order_by("id")

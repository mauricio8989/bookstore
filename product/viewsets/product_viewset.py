from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework.viewsets import ModelViewSet
from product.models import Product
from product.serializers import ProductSerializer

class ProductViewSet(ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer
    def get_queryset(self):
        return Product.objects.all()
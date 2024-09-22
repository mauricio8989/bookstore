import json
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from django.urls import reverse

from product.factories import ProductFactory, CategoryFactory
from order.factories import UserFactory
from product.models import Product

class TestProductViewSet(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = UserFactory()

        self.product = ProductFactory(title='pro controller', price=200.00,)

    def test_get_all_products(self):
        response = self.client.get(
            reverse('product-list', args=['v1'])
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        product_data = json.loads(response.content)

        self.assertEqual(product_data['results'][0]['title'], self.product.title)
        self.assertEqual(product_data['results'][0]['price'], self.product.price)
        self.assertEqual(product_data['results'][0]['active'], self.product.active)

    def test_create_product(self):
        category = CategoryFactory()
        data = json.dumps({
            'title': 'Notebook',
            'price': 800.00,
            'categories_id': [category.id]
        })

        response = self.client.post(
            reverse('product-list', args=['v1']),
            data=data,
            content_type='application/json',
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        created_product = Product.objects.get(title='Notebook')

        self.assertEqual(created_product.title, 'Notebook')
        self.assertEqual(created_product.price, 800.00)
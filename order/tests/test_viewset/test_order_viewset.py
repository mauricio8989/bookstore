import json
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from django.urls import reverse

from product.factories import ProductFactory, CategoryFactory
from order.factories import OrderFactory, UserFactory
from order.models import Order

class TestOrderViewSet(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = UserFactory()  # Criação do usuário para autenticação
        self.client.force_authenticate(user=self.user)  # Autenticando o usuário

        self.category = CategoryFactory(title='technology')
        self.product = ProductFactory(title='mouse', price=100, categories=[self.category])
        self.order = OrderFactory(product=[self.product])

    def test_order(self):
        response = self.client.get(
            reverse('order-list', args=['v1'])
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        order_data = response.json() #Usar response.json() em vez de json.loads
        self.assertEqual(order_data['results'][0]['product'][0]['title'], self.product.title)
        self.assertEqual(order_data['results'][0]['product'][0]['price'], self.product.price)
        self.assertEqual(order_data['results'][0]['product'][0]['active'], self.product.active)
        self.assertEqual(order_data['results'][0]['product'][0]['categories'][0]['title'], self.category.title)

    def test_create_order(self):
        user = UserFactory()  # Criando um usuário
        self.client.force_authenticate(user=user) #Autenticando o usuário

        product = ProductFactory()
        data = json.dumps({
            'products_id': [product.id], #Certificar de que é uma lista
            'user': user.id
        })

        response = self.client.post(
            reverse('order-list', args=['v1']),
            data=data,
            content_type='application/json'
        )

        if response.status_code != status.HTTP_201_CREATED:
            print("Response content:", response.content)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        created_order = Order.objects.get(user=user)

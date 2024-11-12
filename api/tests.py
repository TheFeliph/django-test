# api/tests.py
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Cliente

class ClienteTests(APITestCase):
    def test_criar_cliente(self):
        url = reverse('cliente-list')
        data = {'nome': 'Cliente Teste', 'email': 'cliente@teste.com'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_listar_clientes(self):
        url = reverse('cliente-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

# api/tests.py
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Cliente
from django.urls import reverse

class ClientePaginationTest(APITestCase):

    def setUp(self):
        for i in range(25):  # Criar 25 clientes para testar a paginação
            Cliente.objects.create(nome=f"Cliente {i}", email=f"cliente{i}@teste.com")

    def test_paginacao(self):
        url = reverse('cliente-list')  # ou o nome correto da URL
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('next', response.data)  # Verifica se há um campo 'next' indicando que há mais páginas
        self.assertIn('previous', response.data)  # Verifica se há um campo 'previous'
        self.assertEqual(len(response.data['results']), 10)  # Verifica se a página inicial contém 10 clientes

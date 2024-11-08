from rest_framework import status
from rest_framework.test import APIClient
from django.test import TestCase

class ClienteTests(TestCase):
    def setUp(self):
        self.client = APIClient()  # Instancia o cliente de API

    def test_criar_cliente(self):
        url = '/api/v1/clientes/'  # Certifique-se de que a URL está correta
        data = {
            'nome': 'João',
            'email': 'joao@example.com',
            'endereco': 'Rua A, 123'
        }
        response = self.client.post(url, data, format='json')  # Envia a requisição POST
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # Verifica se o cliente foi criado

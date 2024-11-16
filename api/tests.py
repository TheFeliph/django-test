from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.test import APITestCase

class ClientePaginationTest(APITestCase):
    def setUp(self):
        # Crie um usuário e gere um token
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = APIClient()
        response = self.client.post('/api/token/', {'username': 'testuser', 'password': 'testpass'})
        self.token = response.data['token']
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)

    def test_paginacao(self):
        # Faça a requisição autenticada
        response = self.client.get('/api/v1/clientes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Verifique se a paginação está funcionando
        self.assertIn('results', response.data)

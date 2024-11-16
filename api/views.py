# api/views.py

from rest_framework import viewsets
from .models import Cliente, Pedido
from .serializers import ClienteSerializer, PedidoSerializer
from rest_framework.permissions import IsAuthenticated


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all().order_by('nome')  # Adicionando ordenação por nome
    serializer_class = ClienteSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all().order_by('id')  # Adicionando ordenação por id (exemplo)
    serializer_class = PedidoSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated]
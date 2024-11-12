from rest_framework import viewsets
from .models import Cliente, Pedido
from .serializers import ClienteSerializer, PedidoSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all().order_by('id')  # Adicionando a ordenação por ID
    serializer_class = ClienteSerializer


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

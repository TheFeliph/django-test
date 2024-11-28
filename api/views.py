from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Cliente
from .serializers import ClienteSerializer  # Criaremos isso no próximo passo


class ClientePagination(PageNumberPagination):
    page_size = 5  # Número de itens por página
    page_size_query_param = 'page_size'
    max_page_size = 20


class ClienteListView(APIView):
    def get(self, request):
        clientes = Cliente.objects.all()
        paginator = ClientePagination()
        paginated_clientes = paginator.paginate_queryset(clientes, request)
        serializer = ClienteSerializer(paginated_clientes, many=True)
        return paginator.get_paginated_response(serializer.data)

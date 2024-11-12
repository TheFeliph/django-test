from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClienteViewSet, PedidoViewSet

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'pedidos', PedidoViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),  # Defina o prefixo corretamente
]

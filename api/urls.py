from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClienteViewSet, PedidoViewSet, api_v1  # Importe a função api_v1
from rest_framework.authtoken.views import obtain_auth_token
from . import views

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'pedidos', PedidoViewSet)

urlpatterns = [
    path('token/', obtain_auth_token, name='api_token_auth'),
    path('v1/', include(router.urls)),  # Suas rotas de ViewSets
    path('api/token/', obtain_auth_token, name='api_token_auth'),
    path('v1/', api_v1),  # Agora a função api_v1 está corretamente importada
    
    path('', views.home, name='home'),
]

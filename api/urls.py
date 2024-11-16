from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClienteViewSet, PedidoViewSet
from rest_framework.authtoken import views
from rest_framework.authtoken.views import obtain_auth_token



router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'pedidos', PedidoViewSet)

urlpatterns = [
    path('token/', obtain_auth_token, name='api_token_auth'),
    path('v1/', include(router.urls)),  # Suas rotas de ViewSets
    path('api/token/', obtain_auth_token, name='api_token_auth'),
]
"""
URL configuration for bookstore_01 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# bookstore_01/urls.py
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# Função para exibir uma página inicial simples na raiz
def home(request):
    return HttpResponse("Bem-vindo à Loja Virtual!")

urlpatterns = [
    path('admin/', admin.site.urls),  # URL da área administrativa do Django
    path('api/', include('api.urls')),  # URL da sua API (assumindo que você tenha uma app chamada api)
    path('', home),  # Adiciona a página inicial na raiz

    path('test/', lambda request: HttpResponse("Testando Docker!")),
]

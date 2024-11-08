from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, related_name='pedidos', on_delete=models.CASCADE)
    produto = models.CharField(max_length=200)
    quantidade = models.IntegerField()
    data_pedido = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.produto} - {self.quantidade}'

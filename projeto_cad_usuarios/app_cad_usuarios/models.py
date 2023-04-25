from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    produto = models.TextField(max_length=255)
    quantidade = models.IntegerField()
    valor = models.DecimalField(max_digits=8, decimal_places=2)

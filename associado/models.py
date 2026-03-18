from django.db import models

# Create your models here.

class Associado(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    ativo = models.BooleanField(default=True, null=False, blank=False)

    def __str__(self):
        # Jeito moderno e sem erros de concatenação:
        return f"{self.nome} - Ativo: {self.ativo}"
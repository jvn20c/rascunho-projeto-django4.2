from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Animal(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    descricao = models.TextField()

    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("animais-detalhes", kwargs={"pk": self.pk})

    def __str__(self):
        return self.nome

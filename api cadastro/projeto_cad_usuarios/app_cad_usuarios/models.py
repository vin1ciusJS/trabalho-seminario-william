from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    sobrenome = models.TextField(max_length=255)
    cpf = models.CharField(max_length=11, unique=True)  # Adiciona o campo CPF com 11 caracteres
    email = models.EmailField(max_length=255, unique=True)
    idade = models.IntegerField()
    telefone = models.CharField(max_length=15)  # Adiciona o campo Telefone com no máximo 15 caracteres
    endereco = models.TextField(max_length=255)
    endereco_imovel = models.TextField(max_length=255)  # Adiciona o campo Endereço do Imóvel
    senha = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'
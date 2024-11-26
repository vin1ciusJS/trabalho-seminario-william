from django.shortcuts import render
from .models import Usuario

def cadastro(request):
    return render(request, 'usuarios/cadastro.html')

def usuarios(request):
    if request.method == "POST":
        novo_usuario = Usuario()
        novo_usuario.nome = request.POST.get('nome')
        novo_usuario.sobrenome = request.POST.get('sobrenome')
        novo_usuario.cpf = request.POST.get('cpf')
        novo_usuario.email = request.POST.get('email')
        novo_usuario.idade = request.POST.get('idade')
        novo_usuario.telefone = request.POST.get('telefone')
        novo_usuario.endereco = request.POST.get('endereco')
        novo_usuario.endereco_imovel = request.POST.get('endereco_imovel')
        novo_usuario.senha = request.POST.get('password')
        novo_usuario.save()

    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    return render(request, 'usuarios/usuarios.html', usuarios)
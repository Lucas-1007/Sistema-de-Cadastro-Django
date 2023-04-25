from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request,'usuarios/home.html')

def usuarios(request):
    novo_usuario = Usuario()
    novo_usuario.produto = request.POST.get('produto')
    novo_usuario.quantidade = request.POST.get('quantidade')
    novo_usuario.valor = request.POST.get('valor')
    novo_usuario.save()
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    return render(request,'usuarios/usuarios.html',usuarios)
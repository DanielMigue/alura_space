from django.shortcuts import render

def index(request):#função responsavel pela pagina principal, o request envia uma requisição
    return render(request, 'galeria/index.html')

def imagem(request):
    return render(request,'galeria/imagem.html')
from django.urls import path
from galeria.views import index, imagem #import o index

urlpatterns = [
    path('', index, name='index'),
    path('imagem/', imagem, name='imagem'),
]


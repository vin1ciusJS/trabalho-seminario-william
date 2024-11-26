from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
    path('',views.cadastro,name='cadastro'),
    path('usuarios/',views.usuarios,name='listagem_usuarios')
]
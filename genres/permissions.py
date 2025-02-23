from rest_framework import permissions
from django.contrib.auth.models import User



# Criando uma classe personalizada de permissões chamada GenrePermissionsClass
class GenrePermissionsClass(permissions.BasePermission):

    # Método que verifica se o usuário tem permissão para acessar um recurso
    def has_permission(self, request, view):
        """
        Este método define a lógica de permissões para a requisição atual.
        Ele retorna True se o usuário tiver permissão para acessar o recurso,
        e False caso contrário.
        """

        # Se o método HTTP da requisição for GET (leitura de dados)
        if request.method in ['GET', ' OPTIONS', 'HEAD']:
            # Verifica se o usuário autenticado tem a permissão 'genres.view_genre'
            # Essa permissão deve estar configurada no sistema de permissões do Django
            return request.user.has_perm('genres.view_genre')

        if request.method == 'POST':
            return request.user.has_perm('genres.add_genre')
        
        # Se não for uma requisição GET, a permissão será negada
        return False
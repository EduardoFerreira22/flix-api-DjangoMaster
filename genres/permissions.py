from rest_framework import permissions
from django.contrib.auth.models import User



# Criando uma classe personalizada de permissões chamada GenrePermissionsClass
class GenrePermissionsClass(permissions.BasePermission):

    # Método que verifica se o usuário tem permissão para acessar um recurso
    def has_permission(self, request, view):

        metodo = request.method
        view_name = view.__class__.__module__
        nome_replace = view_name.split(".")[0]
        if nome_replace.endswith('s'):
            nome_replace = nome_replace[:-1]
            print(nome_replace)
        usuario = request.user
        print(usuario)
        print(metodo)
        print(nome_replace)

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

        if request.method in ['PATCH', 'PUT']:
 
            return request.user.has_perm('genres.change_genre')
        
        if request.method == 'DELETE':
            return request.user.has_perm('genres.delete_genre')
        
        # Se não for uma requisição GET, a permissão será negada
        return False
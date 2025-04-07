from rest_framework import generics, permissions

method_actions = {'GET':'view', 'OPTIONS':'view', 'HEAD':'view', 'POST':'add', 'PATCH':'change', 'PUT':'change', 'DELETE':'delete'}
# Criando uma classe personalizada de permissões chamada GenrePermissionsClass
class GlobalPermissionsClass(permissions.BasePermission):
    
    def has_permission(self, request, view):
        model_permission_codname = self.__get_model_permission_name(
            method=request.method,
            view=view,
        )
        print(model_permission_codname)
        if not model_permission_codname:
            return False
        return request.user.has_perm(model_permission_codname)
    
    def __get_model_permission_name(self, method, view):
        try:
            model_name = view.queryset.model._meta.model_name
            app_label = view.queryset.model._meta.app_label
            action = self.__get_action_sufix(method=method)
            return f'{app_label}.{action}_{model_name}'
        except AttributeError:
            return None
    def __get_action_sufix(self, method):
        method_actions = {
            'GET':'view', 
            'OPTIONS':'view', 
            'HEAD':'view', 
            'POST':'add', 
            'PATCH':'change', 
            'PUT':'change', 
            'DELETE':'delete'
        }
        #Ler o dicionário e pega o método que está vindo na requisição.
        return method_actions.get(method, '') 

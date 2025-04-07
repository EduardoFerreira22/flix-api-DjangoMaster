from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from actors.models import Actor
from actors.serializers import ActorSerializer
from app.permissions import GlobalPermissionsClass


class ActorCreateListView(generics.ListCreateAPIView):
    """
    IsAuthenticated: verifica se o usuário está autenticado para poder utilizar a API.
    IsAdminUser: Verifica se esse usuário tem a permissão de ADMIN.
    IsAuthenticatedOrReadOnly: permite que o usuário acesse apenas os SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS') permite apenas GET, HEAD, OPTIONS.
    """
    permission_classes = (IsAuthenticated, GlobalPermissionsClass)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    


class ActorRetrieverUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
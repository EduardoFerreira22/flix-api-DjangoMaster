from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import generics
from movies.models import Movies
from movies.serializers import MovieSerializer
from app.permissions import GlobalPermissionsClass



class MovieCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalPermissionsClass)
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer



class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalPermissionsClass)
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer
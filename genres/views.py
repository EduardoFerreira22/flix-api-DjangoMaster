from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from genres.models import Genre
from genres.serializers import GenreSerializer
from app.permissions import GlobalPermissionsClass

#Functions views
"""
#criação de Api usando metódos do Django
@csrf_exempt
def genre_create_list_view(request): #recebe a requisição

    if request.method == 'GET':
        genres = Genre.objects.all() #Busca todos os objetos do Model Genres da tabela do banco de dados
        data = [{'id': genre.id, 'name':genre.name} for genre in genres] # Variável data recebe uma lista de objetos(dicionários)
        
        return JsonResponse(data, safe=False)#argumento safe=False para a class JsonResponse saber que esses são dados que precisarão ser serializados em Json

    elif request.method == 'POST':

        Pega os dados que o usuário está enviando no body em formato de json 
        decodifica para utf-8 e salva na váriavel data

        data = json.loads(request.body.decode('utf-8'))
        new_genre = Genre(name=data['name'])
        new_genre.save()
        return JsonResponse(
            {'id': new_genre.id, 'name': new_genre.name},
            status=201,
        )


@csrf_exempt
def genre_detail_view(request, pk):
    genre = get_object_or_404(Genre, pk=pk)# Verifica se o objeto existe no banco de dados se não existir retorna o erro 404
    if request.method == 'GET':
        print(pk, genre)
        data = {'id': genre.id, 'name': genre.name}
        return JsonResponse(data)
    
    elif request.method == 'PUT':
        data = json.loads(request.body.decode('utf-8'))
        genre.name = data['name']
        genre.save()

        return JsonResponse(
            {'id': genre.id, 'name': genre.name}
            
        )

    elif request.method == 'DELETE':
        genre.delete()
        return JsonResponse(
            {'mensage': 'Gênero excluído com sucesso!'},
            status=204,
        )
"""

#ClassApiViews
#View para buscar todos os gêneros no banco de dados e criar novos Gêneros no banco de dados
class GenreCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalPermissionsClass)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

#View para Atualizar e apagar dados
class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalPermissionsClass)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
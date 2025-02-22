from django.db.models import Avg
from rest_framework import serializers
from movies.models import Movies


#Utilizando o Serializer diretamente, seria uma forma mais arcaíca pois teremos que informar todos os campos manualmente

#O Model Serializer nos permite utilizar uma classe automatizada que facilita e agiliza o código
class MovieSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True) # Campo calculado diz para o serializer que além de todos os campos que está trazendo, adicione o campo rate e sfaça algum calculo

    class Meta:
        model = Movies
        fields = '__all__'

    def get_rate(self, obj): # segue o padrão do Django get_nome do campo nesse caso o rate
        #Pegue todos os reviews agregue o campo 'stars' e faça o calculo da média
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']
        
        if rate:
            return round(rate, 1)

        return None
        # reviews = obj.reviews.all()

        # if reviews: # Verica se o filme obteve avaliações
        #     sum_reviews = 0 # Inicializa a variável em zero

        #     for review in reviews: # Faz um for em todos os reviews
        #         sum_reviews += review.stars # Pegas os reviews e soma(agrega um ao outro)

        #     reviews_count = reviews.count()#  Conta a quantidade de avaliações 
        #     print(reviews_count)

        #     return round(sum_reviews / reviews_count, 1 )#CASAS DECIMAIS) # O metódo Round faz o arredondamento de números floats


        return None
    #Criando validações de campos
    def validate_release_date(self, value):
        if value.year < 1920:
            raise serializers.ValidationError('A data de lançamento não pode ser anterior a 1990.')
        return value
    
    def validate_resume(self, value):
        if len(value) > 800 :
            raise serializers.ValidationError(f'O resumo contém {len(value)} caracteres.O resumo não deve ser maior que 200 caracteres.')
        return value
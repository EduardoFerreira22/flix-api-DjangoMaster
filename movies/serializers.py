from rest_framework import serializers
from movies.models import Movies


#Utilizando o Serializer diretamente, seria uma forma mais arcaíca pois teremos que informar todos os campos manualmente

#O Model Serializer nos permite utilizar uma classe automatizada que facilita e agiliza o código
class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movies
        fields = '__all__'

    #Criando validações de campos
    def validate_release_date(self, value):
        if value.year < 1960:
            raise serializers.ValidationError('A data de lançamento não pode ser anterior a 1990.')
        return value
    
    def validate_resume(self, value):
        if len(value) > 200:
            raise serializers.ValidationError(f'O resumo contém {len(value)} caracteres.O resumo não deve ser maior que 200 caracteres.')
        return value
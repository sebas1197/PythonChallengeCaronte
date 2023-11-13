from rest_framework import serializers
from .models import DetailPokemon, Pokemon

class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = '__all__'  

class DetailPokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailPokemon
        fields = '__all__'  
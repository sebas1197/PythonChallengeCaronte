from decouple import config
import requests
from rest_framework import viewsets
from .serializer import PokemonSerializer
from .models import Pokemon
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

pokemon_list = []


class PokemonViewSet(viewsets.ModelViewSet):
    api_url = config('URL_POKE_API')
    api_data = requests.get(api_url).json()

    try:
        for general_pokemon in api_data['results']:
            name = general_pokemon['name']
            link = general_pokemon['url']
            pokemon_detail = requests.get(link).json()
            current = pokemon_detail['id']
            image = pokemon_detail['sprites']['front_default']
            go_specific_pokemon = config('URL_DETAIL_POKEMON') + str(pokemon_detail['id'])
            abilities = len(pokemon_detail['abilities'])
            pokemon = Pokemon(current=current, name=name, image=image, abilities=abilities, link=link, go_specific_pokemon=go_specific_pokemon)
            pokemon_list.append(pokemon)
    except Exception as e:
        print(e)

    try:
        Pokemon.objects.bulk_create(pokemon_list)
    except Exception as e:
        print(e)

    limit = len(Pokemon.objects.all())
    queryset = Pokemon.objects.all()[limit-20:]
    serializer_class = PokemonSerializer
    pagination_class = LimitOffsetPagination

class DetailPokemonViewSet(viewsets.ModelViewSet):
    serializer_class = PokemonSerializer

    def retrieve(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')

        try:
            pokemon = next(pokemon for pokemon in pokemon_list if pokemon.current == pk)
            serializer = self.get_serializer(pokemon)
            return Response(serializer.data)
        except Exception as e:
            print(e)
            return Response({'detail': 'Not found.'}, status=404)
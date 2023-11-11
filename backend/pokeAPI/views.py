from decouple import config
import requests

from .serializer import DetailPokemonSerializer, PokemonSerializer
from .models import DetailPokemon, Pokemon
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from rest_framework.decorators import api_view

@api_view(('GET',))
def getAll(request):
    api_url = config('URL_POKE_API')
    api_data = requests.get(api_url).json()
    pokemon_list = []
    
    for general_pokemon in api_data['results']:
        name = general_pokemon['name']
        link = general_pokemon['url']
        pokemon_detail = requests.get(link).json()
        image = pokemon_detail['sprites']['front_default']
        abilities = len(pokemon_detail['abilities'])

        try:
            pokemon = Pokemon(name=name, link=link, image=image, abilities=abilities)
            pokemon_list.append(pokemon)
        except Exception as e:
            print(e)
            return HttpResponse('Error en el listado de pokemones')
    
    try:
        return JsonResponse(PokemonSerializer(pokemon_list, many=True).data, safe=False)
    except Exception as e:  
        print(e)
        return HttpResponse('Error en el listado de pokemones')

@api_view(('GET',))
def getDetails(request, id):
    api_url = config('URL_POKE_API')
    api_data = requests.get(api_url + id).json()
    pokemon_list = []

    try:
        pokemon = DetailPokemon(
            name =  api_data['name'],
            image = api_data['sprites']['front_default'],
            abilities = len(api_data['abilities']),
            link = api_data['forms'][0]['url'],
            base_experience = api_data['base_experience'], 
            height = api_data['height'],
            weight = api_data['weight'],
            _id = api_data['id'],
            is_default = api_data['is_default'],
            order = api_data['order'],
         )
        
        for move in api_data['moves']:
            pokemon.moves += move['move']['name'] + ', '

        for type in api_data['types']:
            pokemon.types += type['type']['name'] + ', '

        pokemon_list.append(pokemon)
    except Exception as e:
        print(e)
        return HttpResponse('Error en el listado detallado de pokemones')
    
    try:
        return JsonResponse(DetailPokemonSerializer(pokemon_list, many=True).data, safe=False)
    except Exception as e:  
        print(e)
        return HttpResponse('Error en el listado detallado de pokemones')
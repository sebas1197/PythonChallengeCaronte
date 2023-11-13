from django.urls import path, include
from rest_framework import routers
from pokeAPI import views

router = routers.DefaultRouter()
router.register(r'pokemons', views.PokemonViewSet)
router.register(r'detail/<int:pk>', views.DetailPokemonViewSet)

urlpatterns = [
    path('', include(router.urls))
]

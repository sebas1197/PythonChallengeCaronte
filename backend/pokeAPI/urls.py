from django.urls import path, include
from rest_framework import routers
from pokeAPI import views
from .views import getAll, getDetails

urlpatterns = [
    path('all/', getAll, name='all'),
    path('details/<str:id>/', getDetails, name='details'),
]
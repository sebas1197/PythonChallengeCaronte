from django.db import models

class Pokemon(models.Model):
    current = models.PositiveIntegerField()
    name =  models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    abilities = models.PositiveIntegerField()
    link = models.URLField()
    go_specific_pokemon = models.URLField()

class DetailPokemon(Pokemon):
    base_experience = models.PositiveIntegerField()
    height = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()
    is_default = models.BooleanField() 
    moves = models.TextField()
    order = models.PositiveIntegerField()
    types = models.TextField()
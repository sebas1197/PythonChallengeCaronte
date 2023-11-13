# Sistema Backend - Software Developer Test

- El proyecto detalla un proyecto en Django para consumir datos de una api (https://pokeapi.co/) tanto de pokemons de vista general con paginación como el detalle de cada uno.

## Pre-requisitos 📋

- Internet.
- Navegador web actual.
- Python versión 3.9.13^ y django 4.2.7^
- Libreria para el uso de variables de entorno 
    ```bash
   pip install python-decouple
- Rest Framework
    ```bash
   pip install djangorestframework


## Ejecución 🛠️

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

- Clonar o descargar el repositorio.
- Abrir una terminal dentro de la carpeta del proyecto y ejecutar el siguiente comando.

    ```bash
   py .\manage.py runserver


## Funcionamiento 🚀

- Una vez que el proyecto este corriendo vistar la url(http://127.0.0.1:8000/api/pokemons/) y se despliegan los datos consumidos de la api de pokemon, paginados en 4 páginas.
- En cada resultado hacer un clic en go_specific_pokemon que redirigira a la url(http://127.0.0.1:8000/api/detail/<pk>) para mostrar los detalles de cada pokemon.
- Las credenciales del superusuario para el login son: 
    - usuario: sebas1197
    - clave: 12345678


## Autor ✒️

* **Ing.Sebastián Landázuri G** 
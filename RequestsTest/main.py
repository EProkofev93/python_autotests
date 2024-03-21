import requests
URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '3ca4b4f15bbecca1f0cf7aef39736cf4'
HEADERS = {'Content-Type' : 'application/json', "trainer_token" : TOKEN}
body = {    
    "name" : "Бобёр",
    "photo" : "https://dolnikov.ru/pokemons/albums/111.png"
}
response = requests.post(url = f'{URL}/pokemons', headers = HEADERS, json = body)
print(response.text)






URL = 'https://api.pokemonbattle.me:9104'
body = {
    
    "pokemon_id": "14478",
    "name": "Флареон",
    "photo" : "https://dolnikov.ru/pokemons/albums/136.png"

}
response = requests.put(url = f'{URL}/pokemons', headers = HEADERS, json = body)
print(response.text)






URL = 'https://api.pokemonbattle.me/v2'
body = {
    "pokemon_id": "14478"
}
response = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADERS, json = body)
print(response.text)
import requests
token = "49fa59775f9f61dad0adc11fc326381c"

response = requests.post('https://api.pokemonbattle.me:9104/pokemons', json={
    "name": "generate",
    "photo": "generate"
}, headers={"Content-Type" : "application/json", "trainer_token": token})

print(response.text)

response_change_name = requests.put('https://api.pokemonbattle.me:9104/pokemons',json={
    "pokemon_id": "11087",
    "name": "newname",
    "photo": "https://dolnikov.ru/pokemons/albums/916.png"
}, headers={"Content-Type" : "application/json", "trainer_token": token})

print(response_change_name.text)

response_pokeball = requests.post('https://api.pokemonbattle.me:9104/trainers/add_pokeball',json={
    "pokemon_id": "11087",
}, headers={"Content-Type" : "application/json", "trainer_token": token})

print(response_pokeball.text)
#connecting to an API using python

import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(pokemon_name):
    url = f"{base_url}pokemon/{pokemon_name.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Successfully retrieved data for {pokemon_name}!")
        data = response.json()
        print(f"Name: {data['name'].title()}")
        print(f"ID: {data.get('id', 'N/A')}")
        print("Types:", ", ".join([t['type']['name'] for t in data['types']]))
        print("Abilities:", ", ".join([a['ability']['name'] for a in data['abilities']]))
    else:        
        print(f"Failed to retrieve data for {pokemon_name}. Status code: {response.status_code}")
        return


pokemon_name = input("Enter the name of a Pokémon: ")
get_pokemon_info(pokemon_name)
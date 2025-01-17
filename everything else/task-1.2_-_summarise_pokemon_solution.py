"""
Exercise 1.2: Summarise Pokémon Details (Solution)
"""

import requests
import json

def summarise_pokemon(name):
    """Fetch and summarise Pokémon details."""
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        name = data['name'].capitalize()
        types = [t['type']['name'] for t in data['types']]
        stats = {stat['stat']['name']: stat['base_stat'] for stat in data['stats']}
        image_url = data['sprites']['front_default']

        print(f"Name: {name}")
        print(f"Types: {', '.join(types)}")
        print("Base Stats:")
        for stat, value in stats.items():
            print(f"  {stat.capitalize()}: {value}")
        print(f"Image URL: {image_url}")
    else:
        print(f"Error: Pokémon '{name}' not found!")

# Example usage
summarise_pokemon("squirtle")

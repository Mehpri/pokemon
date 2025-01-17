"""
Exercise 1.1: Fetch and Display a Pokémon (Solution)
"""

import requests
import json

def fetch_pokemon(name):
    """Fetch Pokémon data from the PokéAPI and display raw JSON."""
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(json.dumps(data, indent=4))  # Pretty-print JSON
    else:
        print(f"Error: Pokémon '{name}' not found!")

# Example usage
fetch_pokemon("squirtle")

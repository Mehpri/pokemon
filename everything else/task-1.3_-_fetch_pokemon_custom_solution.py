"""
Exercise 1.3: Custom Output (Raw vs Summary) (Solution)
"""

import requests
import json

def fetch_pokemon_custom(name, display_raw=False):
    """Fetch Pokémon details and display either raw JSON or a summary."""
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()

        if display_raw:
            print(json.dumps(data, indent=4))
        else:
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
fetch_pokemon_custom("squirtle")  # Display summary by default
# fetch_pokemon_custom("squirtle", display_raw=True)  # Display raw JSON

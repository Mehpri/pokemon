"""
Exercise 2.1: Create a Team Class and Add Pokémon (Solution)
"""

import requests

class Team:
    def __init__(self):
        """Initialize an empty team."""
        self.members = []
    
    def add_pokemon(self, name):
        """Add a Pokémon to the team."""
        # Check if the team already has 6 Pokémon
        if len(self.members) >= 6:
            print("Cannot add more Pokémon. The team is already full (6 Pokémon max)!")
            return
        
        # Check if the Pokémon is already in the team
        if name.lower() in [pokemon['name'].lower() for pokemon in self.members]:
            print(f"{name.capitalize()} is already in your team!")
            return
        
        # Fetch Pokémon data from the PokéAPI
        url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            # Extract necessary details (name, types, image URL)
            pokemon_info = {
                'name': data['name'].capitalize(),
                'types': [t['type']['name'] for t in data['types']],
                'image_url': data['sprites']['front_default']
            }
            # Add the Pokémon to the team
            self.members.append(pokemon_info)
            print(f"{pokemon_info['name']} has been added to your team.")
        else:
            # Print an error message if the Pokémon is not found
            print(f"Error: Pokémon '{name}' not found!")

# Example usage
if __name__ == "__main__":
    team = Team()
    team.add_pokemon("squirtle")
    team.add_pokemon("charmander")
    team.add_pokemon("bulbasaur")
    team.add_pokemon("squirtle")  # Attempt to add duplicate
    team.add_pokemon("mewtwo")
    team.add_pokemon("eevee")
    team.add_pokemon("ho-oh")
    team.add_pokemon("pikachu")    # Attempt to add beyond limit

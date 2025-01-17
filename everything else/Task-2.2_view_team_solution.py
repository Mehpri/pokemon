"""
Exercise 2.2: View the Current Team (Solution)
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
    
    def view_team(self):
        """View the current team with details."""
        # Check if the team is empty
        if not self.members:
            print("Your team is currently empty.")
            return
        
        # Print the team members with their details
        print("Your Team:")
        for idx, pokemon in enumerate(self.members, 1):
            print(f"{idx}. {pokemon['name']} (Types: {', '.join(pokemon['types'])})")
            print(f"   Image URL: {pokemon['image_url']}")

# Example usage
if __name__ == "__main__":
    team = Team()
    team.add_pokemon("squirtle")
    team.add_pokemon("charmander")
    team.view_team()

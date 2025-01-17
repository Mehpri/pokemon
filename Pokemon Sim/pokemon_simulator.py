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
# summarise_pokemon("squirtle")

# start of the battle sim

def calculate_stat(base_stat, level=50, iv=15, ev=85):
    """Calculate Pokémon's stat at given level."""
    return int(((2 * base_stat + iv + (ev / 4)) * level / 100) + 5)

def calculate_hp(base_stat, level=50, iv=15, ev=85):
    """Calculate Pokémon's HP at given level."""
    return int(((2 * base_stat + iv + (ev / 4)) * level / 100) + level + 10)

def calculate_damage(attacker_stats, defender_stats, level=50, base_power=60):
    """Calculate battle damage using standard formula."""
    return int((((2 * level * 0.4 + 2) * attacker_stats['attack'] * base_power) 
                / (defender_stats['defense'] * 50)) + 2)

def fetch_pokemon_data(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch data for {name}: {response.status_code}")

def simulate_battle(pokemon1, pokemon2):
    """Simulate a battle between two Pokémon."""
    # Fetch Pokémon Data
    data1 = fetch_pokemon_data(pokemon1)
    data2 = fetch_pokemon_data(pokemon2)

    # Calculate Initial Stats
    stats1 = {stat['stat']['name']: (calculate_stat(stat['base_stat']) if stat['stat']['name'] != 'hp' else calculate_hp(stat['base_stat'])) for stat in data1['stats']}
    stats2 = {stat['stat']['name']: (calculate_stat(stat['base_stat']) if stat['stat']['name'] != 'hp' else calculate_hp(stat['base_stat'])) for stat in data2['stats']}

    # Initialise Battle Display
    print(f"Battle Start! {pokemon1.capitalize()} vs {pokemon2.capitalize()}")
    print(f"{pokemon1.capitalize()} HP: {stats1['hp']}")
    print(f"{pokemon2.capitalize()} HP: {stats2['hp']}")
    print("---------------------------")

    # Determine First Attacker
    if stats1['speed'] >= stats2['speed']:
        attacker, defender = pokemon1.capitalize(), pokemon2.capitalize()
        attacker_stats, defender_stats = stats1, stats2
    else:
        attacker, defender = pokemon2.capitalize(), pokemon1.capitalize()
        attacker_stats, defender_stats = stats2, stats1

    print(f"{attacker} attacks first!")
    print("---------------------------")

    # Battle Loop
    round_number = 1
    while attacker_stats['hp'] > 0 and defender_stats['hp'] > 0:
        print(f"Round {round_number}")
        damage = calculate_damage(attacker_stats, defender_stats)
        defender_stats['hp'] -= damage

        print(f"{attacker} deals {damage} damage to {defender}.")
        if defender_stats['hp'] <= 0:
            defender_stats['hp'] = 0
            print(f"{defender} has fainted!")
            break

        print(f"{defender} HP remaining: {defender_stats['hp']}")
        print("---------------------------")

        # Swap roles
        attacker, defender = defender, attacker
        attacker_stats, defender_stats = defender_stats, attacker_stats
        round_number += 1

    # End Battle
    print("Battle Over!")
    print(f"The winner is {attacker}!")

if __name__ == "__main__":
    simulate_battle("eevee", "jigglypuff")
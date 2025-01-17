

# Task 3: Pokémon Battle Simulator

## Overview
This task involves building a Pokémon Battle Simulator. Fetch Pokémon stats using the PokéAPI and simulate battles with logic based on their attributes.

## Learning Objectives
- Compare and calculate Pokémon stats.
- Implement a turn-based battle simulation.
- Add randomness for unpredictability (stretch goal).

## Exercises

### Exercise 3.1: Compare Pokémon Stats
- **Goal**: Fetch and calculate stats for two Pokémon, then compare their attributes.
- **Key Features**:
  - Use base stats (attack, defense, speed) at level 50.
  - Display which Pokémon has higher stats in each category.

### Exercise 3.2: Simulate a Turn-Based Battle
- **Goal**: Implement a simple turn-based battle between two Pokémon.
- **Key Features**:
  - Use speed stats to determine the first attacker.
  - Alternate attacks until one Pokémon's HP reaches 0.
  - Display battle details and declare the winner.

### Exercise 3.3: Add Random Events (Stretch Goal)
- **Goal**: Introduce randomness like critical hits or misses.
- **Key Features**:
  - Add a chance for double damage (critical hit) or no damage (miss).
  - Display events dynamically during the battle.

## Example Commands
```python
simulate_battle("eternatus", "palkia")
simulate_battle_with_randomness("ho-oh", "necrozma")

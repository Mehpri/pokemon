# Task 2: Build Your Pokémon Team

## Overview
In this task, you will create a Pokémon team builder. Using the PokéAPI, you will fetch data, store a team of Pokémon, and perform actions like adding, viewing, and removing Pokémon.

## Learning Objectives
- Learn object-oriented programming in Python.
- Fetch and manipulate API data.
- Implement data validation and constraints.

## Exercises

### Exercise 2.1: Create a Team Class
- **Goal**: Build a class to manage Pokémon teams.
- **Key Features**:
  - Initialise an empty team.
  - Add a Pokémon using its name from the PokéAPI.
  - Validate Pokémon names and enforce a maximum team size of 6.

### Exercise 2.2: View the Current Team
- **Goal**: Implement a method to display your Pokémon team.
- **Key Features**:
  - Show each Pokémon’s name, type(s), and image URL.

### Exercise 2.3: Remove Pokémon from the Team
- **Goal**: Add functionality to remove Pokémon by name.
- **Key Features**:
  - Handle errors when attempting to remove non-existent Pokémon.

## Example Commands
```python
team = Team()
team.add_pokemon("mewtwo")
team.view_team()
team.remove_pokemon("pikachu")

## Additional Resources

- [PokéAPI Documentation](https://pokeapi.co/docs/v2)
- [Python OOP Documentation](https://docs.python.org/3/tutorial/classes.html)
---

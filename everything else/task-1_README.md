# Task 1: Fetching and Displaying Pokémon Data

## Overview
This task will guide you through fetching data from the PokéAPI and displaying it in various formats. You'll learn to interact with a real-world API, parse JSON responses, and extract specific information.

The task is divided into three exercises:
1. **Exercise 1.1**: Fetch and display the raw JSON response for a Pokémon.
2. **Exercise 1.2**: Extract and summarise key details about a Pokémon.
3. **Exercise 1.3**: Customise the output to toggle between raw JSON and a summary.

---

## Learning Objectives
- **HTTP Requests**: Learn how to make GET requests using Python's `requests` library.
- **JSON Handling**: Parse and pretty-print JSON responses.
- **Data Extraction**: Extract specific fields from JSON data and format them for display.
- **Function Parameters**: Use parameters to customise function behaviour.

---

## Exercises

### Exercise 1.1: Fetch and Display Raw JSON
- **Goal**: Fetch data for a Pokémon (e.g., Squirtle) and display the entire JSON response in a human-readable format.
- **Hints**:
  - Use `requests.get(url)` to fetch data from the API.
  - Convert the response to JSON using `.json()`.
  - Use `json.dumps(data, indent=4)` to pretty-print the JSON.

### Exercise 1.2: Extract and Summarise Pokémon Details
- **Goal**: Extract specific details (e.g., name, types, base stats, and image URL) from the JSON response and display them.
- **Hints**:
  - Use `data['types']` to get Pokémon types (use a loop to extract them).
  - Use `data['stats']` for base stats (store them in a dictionary).
  - Use `data['sprites']['front_default']` for the image URL.

### Exercise 1.3: Custom Output (Raw vs Summary)
- **Goal**: Modify the function to allow toggling between displaying the full JSON and the summarised details using a parameter.
- **Hints**:
  - Add a parameter `display_raw` to your function.
  - Use an `if` condition to decide whether to pretty-print the full JSON or display a summary.

---

## Useful Resources
1. [PokéAPI Documentation](https://pokeapi.co/docs/v2)
   - Learn about available endpoints and data structures.
2. [Python Requests Library Documentation](https://docs.python-requests.org/)
   - Understand how to make HTTP requests.
3. [Python JSON Library](https://docs.python.org/3/library/json.html)
   - Learn how to parse and manipulate JSON data.

---

## Common Issues and Troubleshooting
1. **404 Error**: Double-check the Pokémon name (case-insensitive but must be spelled correctly).
2. **Timeouts**: The API may occasionally experience downtime. Retry after some time.
3. **Missing Libraries**:
   - Install missing libraries with `pip install requests`.

---

## Example Outputs

### Example 1: Raw JSON Output
**Command**:
```python
fetch_pokemon("squirtle")
# output
{
    "name": "squirtle",
    "types": [
        {"type": {"name": "water"}}
    ],
    ...
}
```
### Example 2: Summary Output
**Command**:
```python
summarise_pokemon("squirtle")
#output
Name: Squirtle
Types: Water
Base Stats:
  Hp: 44
  Attack: 48
  Defense: 65
  Special-attack: 50
  Special-defense: 64
  Speed: 43
Image URL: https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/7.png
```
---
## Stretch Goals

  -  Enhanced Error Handling: Add functionality to handle errors more gracefully (e.g., invalid Pokémon names).
  -  Interactive Input: Allow us to input Pokémon names interactively instead of hardcoding them.
  - Additional Parameters: Implement additional parameters to filter or sort the data based on specific criteria.
  ---
  ---
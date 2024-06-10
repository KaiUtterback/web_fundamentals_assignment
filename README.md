Sure, here's a README for the two Python projects described above.

---

# Pokémon and Space Data Fetcher

This repository contains two Python scripts:

1. **Pokémon Data Fetcher**: Fetches and displays information about specified Pokémon from the Pokémon API.
2. **Space Data Fetcher**: Fetches and displays information about planets in our solar system from the Solar System OpenData API.

## Pokémon Data Fetcher

### Description
This script fetches data for three specified Pokémon (Bulbasaur, Charmander, and Squirtle) from the Pokémon API. It prints their names, abilities, and calculates the average weight of these Pokémon.

### Usage
1. Ensure you have Python installed on your system.
2. Install the `requests` library if you haven't already:
    ```sh
    pip install requests
    ```
3. Run the script:
    ```sh
    python pokemon_data_fetcher.py
    ```

### Script: `pokemon_data_fetcher.py`
```python
import requests

def fetch_pokemon_data(pokemon_name):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve data for {pokemon_name}. Status code: {response.status_code}")
        return None

def calculate_average_weight(pokemon_list):
    total_weight = sum(pokemon['weight'] for pokemon in pokemon_list)
    return total_weight / len(pokemon_list)

pokemon_names = ["bulbasaur", "charmander", "squirtle"]
pokemon_data_list = []

for name in pokemon_names:
    data = fetch_pokemon_data(name)
    if data:
        pokemon_data_list.append(data)
        print(f"Name: {data['name'].capitalize()}")
        abilities = [ability['ability']['name'] for ability in data['abilities']]
        print("Abilities:")
        for ability in abilities:
            print(f"- {ability}")
        print()

if pokemon_data_list:
    average_weight = calculate_average_weight(pokemon_data_list)
    print(f"Average Weight: {average_weight} hectograms")
```

## Space Data Fetcher

### Description
This script fetches data about planets in our solar system from the Solar System OpenData API. It prints each planet's name, mass, and orbit period, and identifies the heaviest planet in the solar system.

### Usage
1. Ensure you have Python installed on your system.
2. Install the `requests` library if you haven't already:
    ```sh
    pip install requests
    ```
3. Run the script:
    ```sh
    python space_data_fetcher.py
    ```

### Script: `space_data_fetcher.py`
```python
import requests

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']
    
    planet_info = []
    
    for planet in planets:
        if planet['isPlanet']:
            name = planet['englishName']
            mass = planet['mass']['massValue'] if planet['mass'] else None
            orbit_period = planet['sideralOrbit'] if planet['sideralOrbit'] else None
            planet_info.append({'name': name, 'mass': mass, 'orbit_period': orbit_period})
            print(f"Planet: {name}, Mass: {mass} x 10^24 kg, Orbit Period: {orbit_period} days")
    
    heaviest_planet = max(planet_info, key=lambda x: x['mass'])
    print(f"\nThe heaviest planet is {heaviest_planet['name']} with a mass of {heaviest_planet['mass']} x 10^24 kg.")

fetch_planet_data()
```

---

Feel free to customize the README further to suit your needs.

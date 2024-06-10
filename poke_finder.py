import requests

# TASK 1

response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")


if response.status_code == 200:
    data = response.json()
    
    name = data['name']
    print(f"Name: {name}")

    abilities = [ability['ability']['name'] for ability in data['abilities']]
    print("Abilities:")
    for ability in abilities:
        print(f"- {ability}")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")

print()


# TASK 2

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

pokemon_names = ["squirtle", "bulbasaur", "charmander"]
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


""" 
pokemon_data = getPoke("Charmander")

if pokemon_data:
    print(f"\n--- {pokemon_data['name'].capitalize()} Pokedex Entry ---")
    for key, value in pokemon_data.items():
        print(f"{key.capitalize()} → {value}")

    print("\n--- Let's catch another one! ---")
    pikachu_data = getPoke("Pikachu")
    if pikachu_data:
        print(f"{pikachu_data['name'].capitalize()} is of type(s): {', '.join(pikachu_data['types'])}")


 """
import requests

def getPoke(poke):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{poke.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()
    return {
        "name": data["name"],
        "height": data["height"],
        "weight": data["weight"],
        "types": [t["type"]["name"] for t in data["types"]]
    }

pokemon = getPoke("Bulbasaur")
for key, value in pokemon.items():
    print(f"{key.title()}: {value}")
print(pokemon)

import requests
""" import requests
""" """ 
pokemon_data = getPoke("Charmander")

if pokemon_data:
    print(f"\n--- {pokemon_data['name'].capitalize()} Pokedex Entry ---")
    for key, value in pokemon_data.items():
        print(f"{key.capitalize()} → {value}")

    print("\n--- Let's catch another one! ---")
    pikachu_data = getPoke("Pikachu")
    if pikachu_data:
        print(f"{pikachu_data['name'].capitalize()} is of type(s): {', '.join(pikachu_data['types'])}") """


"""


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

 """
import os
import requests

API_KEY = os.getenv("9d36553e31c1df00a176d6891a0704a5")

BASE_URL = "https://v3.football.api-sports.io"

HEADERS = {
    "x-apisports-key": '9d36553e31c1df00a176d6891a0704a5'
}


def get_teams(league_id=39, season=2024):
    url = f"{BASE_URL}/teams?league={league_id}&season={season}"
    response = requests.get(url, headers=HEADERS)
    data = response.json()

    print("\n Teams:\n")

    for team in data.get("response", []):
        name = team["team"]["name"]
        country = team["team"]["country"]
        print(f"{name} ({country})")


def get_standings(league_id=39, season=2024):
    url = f"{BASE_URL}/standings?league={league_id}&season={season}"
    response = requests.get(url, headers=HEADERS)
    data = response.json()

    print("\n League Standings:\n")

    standings = data["response"][0]["league"]["standings"][0]

    for team in standings:
        rank = team["rank"]
        name = team["team"]["name"]
        played = team["all"]["played"]
        points = team["points"]

        print(f"{rank}. {name} | {points} pts | Played: {played}")


def code():
    while True:
        print("\n Your Soccer App")
        print("1. View Teams")
        print("2. View Standings")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            get_teams()
        elif choice == "2":
            get_standings()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    code()
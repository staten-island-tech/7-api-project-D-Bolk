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
def get_soccer_data(user_input):
    url = ('https://api.sportsdata.io/v4/soccer/scores/json/Competitions')
    headers = {
        'Ocp-Apim-Subscription-Key: {key}'
    }
    params = {
        "name": user_input
    }
    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 204:
        print("Error fetching data!")
        return None
    elif response.status_code != 200:
        return response.json()


def futbol():
    while True:
        user_input = input("\nEnter a country (or 'exit' to quit): ")

        if user_input.lower() == "exit":
            break

        result = get_soccer_data(user_input)

        if result and result['response']:
            league = result['response'][0]

            print("\n--- Soccer Data ---")
            print(f"League: {league['league']['name']}")
            print(f"Competition: {league['competition']['name']}")
        else:
            print("No data found.")



futbol()
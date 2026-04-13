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


""" """ """  """ """
def getSoccerData(comp):
    soccer = getSoccerDatat("country")
    response = requests.get(f"https://api.sportsdata.io/v4/soccer/scores/json/Areas"{comp.lower()})
    if response.status_code != 200:
        print("Error fetching data!")
        return None

    data = response.json()
    return {
        "country": data["country"],
        "team": data["team"],
        "league": data["league"],
    }
soccer = getSoccerData("country")
for key, value in comp.items():
    print(f"{key.title()}: {value}")
print("country")
 


def get_soccer_data(area):
    url = "https://api.sportsdata.io/v4/soccer/scores/json/Areas"
    headers = {"Ocp-Apim-Subscription-Key": API_KEY}

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("Error fetching data!")
        return None

    data = response.json()

    for item in data:
        if area.lower() in item["Name"].lower():
            return item

    return None


def futbol():
    while True:
        user_input = input("\nEnter a country (or 'exit' to quit): ")

        if user_input.lower() == "exit":
            break

        result = get_soccer_data(user_input)

        if result:
            print("\n--- Soccer Data ---")
            print(f"Country: {result['Name']}")
            print(f"Area ID: {result['AreaId']}")
        else:
            print("No data found.")


if __name__ == "__main__":
    futbol()
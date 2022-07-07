import requests
import pprint

# names for adding with a loop to view the results
names = [
    "metagross",
    "scizor",
    "doublade",
    "rockruff",
    "trumbeak",
    "heracross",
    "crobat",
    "machamp",
    "cryogonal",
    "raikou",
    "rayquaza",
    "wobbuffet",
    "zygarde",
    "fraxure",
    "electabuzz",
    "incineroar",
    "nidoking",
    "basculegion",
    "flygon",
    "pignite",
    "quilava",
    "toxapex",
    "marshadow",
    "inteleon",
    "tornadus",
    "gastly",
    "perrserker",
    "staskataka",
    "psyduck",
    "frosmoth",
]


class Pokemon:
    def __init__(
        self,
        name,
        p_type,
        height=0,
        weight=0,
        hp=0,
        attack=0,
        defense=0,
        speed=0,
        abilities=[],
    ):
        self.name = name
        self.type = p_type
        self.height = height
        self.weight = weight
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.abilities = abilities


class Pokedex:
    def __init__(self, name):
        self.name = name.lower()

        # make api call with the name
        api_url = f"https://pokeapi.co/api/v2/pokemon/{self.name}"
        data = requests.get(api_url).json()

        # keep a list of the pokemon in the pokedex
        self.pokemon = []

        # create pokemon and add it to the list
        pokemon = Pokemon(
            name=data["name"],
            p_type=data["types"][0]["type"]["name"],
            height=data["height"],
            weight=data["weight"],
            hp=data["stats"][0]["base_stat"],
            attack=data["stats"][1]["base_stat"],
            defense=data["stats"][2]["base_stat"],
            speed=data["stats"][5]["base_stat"],
            abilities=[a["ability"]["name"] for a in data["abilities"]],
        )

        self.pokemon.append(pokemon)

    @classmethod
    def run(cls):
        poke = input("Enter a name: ")
        return cls(poke)


# how to make (instantiate) Pokedex with an add() to add Pokemon rather than in __init__()
# why need to save Pokedex classmethod to variable?
# how to organize and sort by "type"?
# how to keep track of types as they come in and then show them all
# how to cycle through a variable num of abilities in the data

Pokedex.run()

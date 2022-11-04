import os
import pandas as pd
from .pokemon import Pokemon


def retrieve_types():
    DATA_PATH = "data"
    POKEMON_DATA_PATH = os.path.join(DATA_PATH, "pokemon.csv")
    TYPE_PATH = os.path.join(DATA_PATH, "pokemon_type.txt")

    pokemon_table = pd.read_csv(POKEMON_DATA_PATH)

    types1 = pokemon_table.Type1
    types2 = pokemon_table.Type2[pokemon_table.Type2.notnull()]

    types = set((*types1, *types2, 'None'))

    text = "\n".join(types)
    with open(TYPE_PATH, "w") as file:
        file.write(text)


def visualize_pokemon(pokemon_id: int):
    """
    Get the id of a pokemon and gives all the informations about him.
    """
    pokemon: Pokemon = Pokemon.get_pokemon(pokemon_id)
    pokemon.display_intel()
    pass



argument_correspondance = {
    "--types": retrieve_types,
    "--visualize": visualize_pokemon
}
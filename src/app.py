from .pokemon import Pokemon



def visualize_pokemon(pokemon_id: int):
    """
    Get the id of a pokemon and gives all the informations about him.
    """
    pokemon: Pokemon = Pokemon.get_pokemon(pokemon_id)
    pokemon.display_intel()
    pass
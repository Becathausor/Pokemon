import os
import matplotlib.pyplot as plt
from .pokemon_type import PokemonType
from .pokemon_exceptions import InvalidPkmn


class Pokemon:
    def __init__(self,
        pokemon_id: int,
        name: str,
        type1: PokemonType,
        type2: PokemonType=None,
        ):

        if type1.isnull():
            raise InvalidPkmn("The pokemon has a null type as a type 1.")

        self.pokemon_id: int = pokemon_id
        self.name: str = name
        self.type1: str = PokemonType(type1)
        self.type2: str = PokemonType(type2)
        
        self.image_path = os.path.join('data', 'images', f'{name}.png')

    def __str__(self):
        return f"{self.pokemon_id}: {self.name}\n  type1: {self.type1}\n  type2: {self.type2}"

    def __repr__(self):
        return f"{self.pokemon_id}: {self.name}\n  type1: {self.type1}\n  type2: {self.type2}"

    def display_intel(self, show_image=False):
        print(self)
        if show_image:
            if not(os.path.exists(self.image_path)):
                raise InvalidPkmn

            plt.imshow(plt.imread(self.image_path))
            plt.show()


import os
import pandas as pd
import matplotlib.pyplot as plt
from .pokemon_type import PokemonType
from .pokemon_exceptions import InvalidPkmnError
# from . import CSV_PATH, IMAGES_PATH


DATA_PATH = "data"
CSV_PATH = os.path.join(DATA_PATH, "pokemon.csv")
TYPE_PATH = os.path.join(DATA_PATH, "pokemon_type.txt")
IMAGES_PATH = os.path.join(DATA_PATH, "images")
DATASETS_PATH = os.path.join(DATA_PATH, "datasets")


class Pokemon:
    pokemon_table = pd.read_csv(CSV_PATH)

    @classmethod
    def get(cls, pokedex_id: int):
        """
        Gets the pokemon from its pokedex id.
        
        Args:
            pokedex_id: int

        Returns:
            Pokemon
        """
        pokemon_line = cls.pokemon_table.loc[pokedex_id - 1]
        if pokemon_line.isnull().any():
            return cls(pokedex_id, pokemon_line.Name, pokemon_line.Type1)
        else:
            return cls(pokedex_id, pokemon_line.Name, pokemon_line.Type1, pokemon_line.Type2)

    def __init__(self,
        pokedex_id: int,
        name: str,
        type1: PokemonType,
        type2: PokemonType=None,
        ):

        if PokemonType(type1).isnull():
            raise InvalidPkmnError("The pokemon has a null type as a type 1.")

        self.pokedex_id: int = pokedex_id
        self.name: str = name
        self.type1: str = PokemonType(type1)
        self.type2: str = PokemonType(type2)
        
        self.image_path = os.path.join(IMAGES_PATH, f'{name}.png')

    def __str__(self):
        return f"{self.pokedex_id}: {self.name}\n  type1: {self.type1}\n  type2: {self.type2}"

    def __repr__(self):
        return f"{self.pokedex_id}: {self.name}\n  type1: {self.type1}\n  type2: {self.type2}"

    def display_intel(self, show_image=False):
        print(self)
        if show_image:
            if not(os.path.exists(self.image_path)):
                raise InvalidPkmnError

            plt.imshow(plt.imread(self.image_path))
            plt.show()


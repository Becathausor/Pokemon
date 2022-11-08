import os
from .pokemon_exceptions import InvalidPkmnTypeError

# from . import TYPE_PATH


DATA_PATH = "data"
CSV_PATH = os.path.join(DATA_PATH, "pokemon.csv")
TYPE_PATH = os.path.join(DATA_PATH, "pokemon_type.txt")
IMAGES_PATH = os.path.join(DATA_PATH, "images")
DATASETS_PATH = os.path.join(DATA_PATH, "datasets")


with open(TYPE_PATH, "r") as file:
    lines = file.readlines()
read_types = {line[:-1] for line in lines}


class PokemonType:
    types = read_types

    def __init__(self, name) -> None:
        if name is None:
            self.name = "Nan"
        elif name in read_types:
            self.name = name
        else:
            raise InvalidPkmnTypeError(
                f"Received a type that hasn't been repertoriated. Received type: {name}"
            )
        pass

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name

    def isnull(self) -> bool:
        return self.name == "Nan"

    pass

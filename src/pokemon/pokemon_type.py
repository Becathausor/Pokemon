import os
from .pokemon_exceptions import InvalidPkmnTypeException


type_table_path = os.join("data", "pokemon_type.txt")
with open(type_table_path, 'r') as file:
    lines = file.readlines()
read_types = set(lines)


class PokemonType:
    types = read_types
    def __init__(self, name) -> None:
        if name in read_types:
            self.name = name
        else:
            raise InvalidPkmnTypeException
        pass

    def __str__(self) -> str:
        return self.name
    
    def __repr__(self) -> str:
        return self.name

    def isnull(self) -> bool:
        return self.name == "None"

    pass

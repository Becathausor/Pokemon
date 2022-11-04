from dataclasses import dataclass
from .pokemon_type import PkmnType

@dataclass
class Pokemon:
    id: int
    name: str
    type1: PkmnType
    type2: PkmnType

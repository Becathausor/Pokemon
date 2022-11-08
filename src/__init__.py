import os
from .app import *

# DATA_PATH = "data"
# CSV_PATH = os.path.join(DATA_PATH, "pokemon.csv")
# TYPE_PATH = os.path.join(DATA_PATH, "pokemon_type.txt")
# IMAGES_PATH = os.path.join(DATA_PATH, "images")
# DATASETS_PATH = os.path.join(DATA_PATH, "datasets")

__all__ = [
    "argument_correspondance",
    "retrieve_types",
    "visualize_pokemon",
    "create_datasets",
    "Dataset",
    # "DATA_PATH",
    # "CSV_PATH",
    # "TYPE_PATH",
    # "IMAGES_PATH",
    # "DATASETS_PATH",
]

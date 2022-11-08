import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pickle import dump, load

# from . import CSV_PATH, IMAGES_PATH

DATA_PATH = "data"
CSV_PATH = os.path.join(DATA_PATH, "pokemon.csv")
TYPE_PATH = os.path.join(DATA_PATH, "pokemon_type.txt")
IMAGES_PATH = os.path.join(DATA_PATH, "images")
DATASETS_PATH = os.path.join(DATA_PATH, "datasets")

table = pd.read_csv(CSV_PATH)

names = table.Name
images = []
ids = list(range(len(names)))
types = list(zip(table.Type1, table.Type2))

for pokemon_name in names:
    try:
        image = plt.imread(os.path.join(IMAGES_PATH, pokemon_name + ".png"))
    except FileNotFoundError:
        image = plt.imread(os.path.join(IMAGES_PATH, pokemon_name + ".jpg"))
    images.append(image)


hash_map = {"id": ids, "name": names, "type": types, "image": images}


class Dataset:
    def __init__(self, features: list[str], labels: list[str]) -> None:
        try:
            self.features = np.array(list(zip((hash_map[key] for key in features))))
            self.labels = np.array(
                list(zip((hash_map[key] for key in labels))), dtype=object
            )
        except Exception:
            print(f"features: {features}")
            print(f"labels: {labels}")
        self._shape = ()

        self.initialize_shape()
        pass

    @property
    def shape(self):
        return self._shape

    def initialize_shape(self):
        features_shape = self.features.shape
        labels_shape = self.labels.shape
        self._shape = features_shape, labels_shape

    def __len__(self):
        return self.shape

    def save(self, path: str) -> None:
        with open(path, "wb") as file:
            dump(self, file)

    @classmethod
    def load(cls, path: str):
        with open(path, "rb") as file:
            dataset = load(file)
        return dataset

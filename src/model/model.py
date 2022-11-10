from pickle import dump, load

class Model:
    def __init__(self):
        pass

    def save(self, path: str) -> None:
        with open(path, "wb") as file:
            dump(self, file)

    @classmethod
    def load(cls, path: str):
        with open(path, "rb") as file:
            dataset = load(file)
        return dataset


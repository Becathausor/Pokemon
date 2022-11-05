import os
import pandas as pd
from .pokemon import Pokemon
from .dataset import Dataset
from .application_exception import ParsingError

def retrieve_types(*args) -> None:
    """
    If it has'nt been done, create a text file in the data directory to indicate the possible pokemon mono-types.
    """
    DATA_PATH = "data"
    POKEMON_DATA_PATH = os.path.join(DATA_PATH, "pokemon.csv")
    TYPE_PATH = os.path.join(DATA_PATH, "pokemon_type.txt")

    if not(os.path.exists(TYPE_PATH)):
        pokemon_table = pd.read_csv(POKEMON_DATA_PATH)

        types1 = pokemon_table.Type1
        types2 = pokemon_table.Type2[pokemon_table.Type2.notnull()]

        types = set((*types1, *types2, 'None'))

        text = "\n".join(types)
        with open(TYPE_PATH, "w") as file:
            file.write(text)
    pass

def visualize_pokemon(*args):
    """
    Get the id of a pokemon and gives all the informations about him.

    Arguments:
        pokemon_id (int): The id number of the pokemon in the National Dex

        show_image (bool): Indicates if we need to display an image of the pokemon 
    """
    pokemon_id: int = int(args[0])
    show_image = bool(args[1])
    pokemon: Pokemon = Pokemon.get(int(pokemon_id))
    pokemon.display_intel(show_image=show_image)
    pass

def split_dataset_arguments(*args):
    """
    Split arguments into two iterators of arguments for feature arguments, label arguments and dataset filename.

    Arguments:
        args (iter[str]): An iterator of string arguments with a separator to distinguish features and labels

    Returns:
        feature_arguments (iter[str])
        label_arguments (iter[str])
        filename (str)
    """
    separator = ":"

    one = " ".join(args)
    features, labels, filename = one.split(sep=separator)
    features = features.split(sep=" ")[:-1]
    labels = labels.split(sep=" ")[1:-1]
    filename = filename.split(sep=" ")[1:][0]
    return features, labels, filename

def create_datasets(*args) -> Dataset:
    """
    Create a dataset and saves it. Takes string arguments to represent feature arguments, label arguments and the filename of registration.
    """
    training_arguments, testing_arguments, filename = split_dataset_arguments(*args)
    dataset = Dataset(training_arguments, testing_arguments)
    dataset.save(os.path.join("data", "datasets", filename))

argument_correspondance = {
    "--types": retrieve_types,
    "--visualize": visualize_pokemon,
    "--create_dataset": create_datasets
}
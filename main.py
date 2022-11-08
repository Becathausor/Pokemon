from src import *
import sys


if __name__ == "__main__":
    arguments = sys.argv
    action = argument_correspondance[arguments[1]]
    if len(arguments) > 2:
        action(*arguments[2:])
    else:
        action()

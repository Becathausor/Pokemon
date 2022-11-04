from src import *
import sys


if __name__ == '__main__':
    arguments = sys.argv
    action = argument_correspondance[arguments[1]]()



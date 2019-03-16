FILE_NAME = "dict.txt"

def read_dictionary():
    with open(FILE_NAME) as f:
        dictionary = f.readlines()
    dictionary = [x.strip() for x in dictionary]
    return dictionary


def read_board():
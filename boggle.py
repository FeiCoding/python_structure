from Trie import *
from collections import defaultdict

DICT_FILE_NAME = "dict.txt"
BOARD_FILE_NAME = "board.txt"


def dictionary_dict(words):
    dictionary = defaultdict(list)
    for word in words:
        if word:
                dictionary[word[0]].append(word)
    return dictionary


def dictionary_trie(words):
    dictionary = Trie()
    for word in words:
        dictionary.insert(words)
    return dictionary


def read_dictionary():
    with open(DICT_FILE_NAME) as f:
        dictionary = f.readlines()
    list_dictionary = [x.strip() for x in dictionary]
    dict_dictionary = dictionary_dict(list_dictionary)
    trie_dictionary = dictionary_trie(list_dictionary)
    return list_dictionary, dict_dictionary, trie_dictionary


def read_board():
    board = []
    count = 0
    with open(BOARD_FILE_NAME) as f:
        lines = f.readlines()
    lines = [line.rstrip('\n') for line in lines]
    for line in lines:
        board.append([x.strip() for x in line.split(',')])
    print(board)
    return board

def boggle_solver(board, list_dictionary, dict_dictionary, trie_dictionary):
    row_len = len(board)
    col_len = len(board)
    found_word = set()
    bool_board = [[False for i in range(col_len)] for j in range(row_len)]
    for i in range(row_len):
        for j in range(col_len):
            


def __main__():
    board = read_board()
    # list_dictionary, dict_dictionary, trie_dictionary = read_dictionary()
    # boggle_solver(board, list_dictionary, dict_dictionary, trie_dictionary)

if __name__ == '__main__':
    __main__()
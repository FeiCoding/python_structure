from Trie import *
from collections import defaultdict
import timeit
from Plotter import *
import Board_builder

BOARD_SIZE = 20
DICT_FILE_NAME = "dict.txt"
BOARD_FILE_NAME = "board.txt"
NAME = ["List", "Dict", "Trie"]


def dictionary_dict(words):
    dictionary = defaultdict(list)
    for word in words:
        if word:
                dictionary[word[0]].append(word)
    return dictionary


def dictionary_trie(words):
    dictionary = Trie()
    for word in words:
        dictionary.insert(word)
    return dictionary


def read_dictionary(dict_type):
    with open(DICT_FILE_NAME) as f:
        dictionary = f.readlines()
    list_dictionary = [x.strip() for x in dictionary]
    if dict_type == "list":
        return list_dictionary
    elif dict_type == "dict":
        dict_dictionary = dictionary_dict(list_dictionary)
        return dict_dictionary
    elif dict_type == "trie":
        trie_dictionary = dictionary_trie(list_dictionary)
        return trie_dictionary


def read_board():
    board = []
    with open(BOARD_FILE_NAME) as f:
        lines = f.readlines()
    lines = [line.rstrip('\n') for line in lines]
    print("The boggle board is:")
    for line in lines:
        board.append([x.strip() for x in line.split(',')])
        print(line)
    return board


def is_safe(i, j, length, visited_board):
    return (0 <= i < length) and (0 <= j < length) and (visited_board[i][j] is False)


def trie_find(root, string, found_word, board, visited_board, i, j, length):
    if root.leaf is True:
        found_word.add(string)
    if is_safe(i, j, length, visited_board):
        visited_board[i][j] = True
        for k in range(len(root.children)):
            if root.children[k] is not None:
                ch = chr(k + ord('a'))
                if is_safe(i, j + 1, length, visited_board) and board[i][j + 1] == ch:
                    trie_find(root.children[k], string + ch, found_word, board, visited_board, i, j + 1, length)
                if is_safe(i, j - 1, length, visited_board) and board[i][j - 1] == ch:
                    trie_find(root.children[k], string + ch, found_word, board, visited_board, i, j - 1, length)
                if is_safe(i + 1, j, length, visited_board) and board[i + 1][j] == ch:
                    trie_find(root.children[k], string + ch, found_word, board, visited_board, i + 1, j, length)
                if is_safe(i - 1, j, length, visited_board) and board[i - 1][j] == ch:
                    trie_find(root.children[k], string + ch, found_word, board, visited_board, i - 1, j, length)
                if is_safe(i - 1, j + 1, length, visited_board) and board[i - 1][j + 1] == ch:
                    trie_find(root.children[k], string + ch, found_word, board, visited_board, i - 1, j + 1, length)
                if is_safe(i - 1, j - 1, length, visited_board) and board[i - 1][j - 1] == ch:
                    trie_find(root.children[k], string + ch, found_word, board, visited_board, i - 1, j - 1, length)
                if is_safe(i + 1, j + 1, length, visited_board) and board[i + 1][j + 1] == ch:
                    trie_find(root.children[k], string + ch, found_word, board, visited_board, i + 1, j + 1, length)
                if is_safe(i + 1, j - 1, length, visited_board) and board[i + 1][j - 1] == ch:
                    trie_find(root.children[k], string + ch, found_word, board, visited_board, i + 1, j - 1, length)
        visited_board[i][j] = False


def find(word, str_index, found_word, board, visited_board, i, j, length):
    if i >= length or i < 0 or j >= length or j < 0 or word[str_index] != board[i][j] or visited_board[i][j] is True:
        return
    visited_board[i][j] = True
    str_index += 1
    if str_index == len(word):
        found_word.add(word)
        visited_board[i][j] = False
        return
    find(word, str_index, found_word, board, visited_board, i + 1, j, length)
    find(word, str_index, found_word, board, visited_board, i - 1, j, length)
    find(word, str_index, found_word, board, visited_board, i, j + 1, length)
    find(word, str_index, found_word, board, visited_board, i, j - 1, length)
    find(word, str_index, found_word, board, visited_board, i - 1, j - 1, length)
    find(word, str_index, found_word, board, visited_board, i - 1, j + 1, length)
    find(word, str_index, found_word, board, visited_board, i + 1, j - 1, length)
    find(word, str_index, found_word, board, visited_board, i + 1, j + 1, length)
    visited_board[i][j] = False


def solve(dict_type, board):
    start_time = timeit.default_timer()
    row_len = len(board)
    col_len = len(board)
    dictionary = read_dictionary(dict_type)
    found_word = set()
    visited_board = [[False for i in range(col_len)] for j in range(row_len)]
    string = ""
    for i in range(row_len):
        for j in range(col_len):
            if dict_type == "list":
                for word in dictionary:
                    if board[i][j] == word[0]:
                        if len(word) > 2:
                            find(word, 0, found_word, board, visited_board, i, j, row_len)
            elif dict_type == "dict":
                for word in dictionary[board[i][j]]:
                    if len(word) > 2:
                        find(word, 0, found_word, board, visited_board, i, j, row_len)
            elif dict_type == "trie":
                pChild = dictionary
                if pChild.root.children[pChild.charToIndex(board[i][j])] is not None:
                    string += board[i][j]
                    root = pChild.root.children[pChild.charToIndex(board[i][j])]
                    trie_find(root, string, found_word, board, visited_board, i, j, row_len)
                    string = ""
    print("Total number of word found in ", dict_type, " dictionary is: ", len(found_word))
    return round(timeit.default_timer() - start_time, 3), found_word


def boggle_solver():
    board = read_board()
    time_list, word_list = solve("list", board)
    time_dict, word_dict = solve("dict", board)
    time_trie, word_trie = solve("trie", board)
    res = []
    return time_list, time_dict, time_trie


def __main__():
    Board_builder.make_board(BOARD_SIZE)
    time_list, time_dict, time_trie = boggle_solver()
    time_ = [time_list, time_dict, time_trie]
    plot = Plotter()
    plot_name = '{0}X{0} Boggle'.format(BOARD_SIZE)
    plot.diagram_plot(time_, NAME, plot_name)


if __name__ == '__main__':
    __main__()


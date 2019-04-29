import random
import numpy
import csv

FILE_NAME = "board.txt"


def make_board(SIZE):
    random_list = list()
    for index in range(0,SIZE * SIZE):
        random_list.append(random.randrange(0,26))
    char_list = list()
    for num in random_list:
        char_list.append(chr(num + ord('a')))
    char_list = numpy.reshape(char_list, (SIZE, SIZE))

    with open(FILE_NAME, 'w', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(char_list)

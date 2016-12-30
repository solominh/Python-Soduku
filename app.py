import solution1
import solution2


def read_test(filepath):
    board = ''
    with open(filepath) as f:
        for line in f:
            board += line.strip()
    return board


def write_result(board, filepath):
    with open(filepath, 'w') as f:
        for i in range(9):
            f.write(str(board[i * 9:i * 9 + 9]))
            f.write('\n')


def convert_stringlist_to_intlist(str_list):
    return [int(x) for x in str_list]
    # return list(map(int, str_list))


import testgenerator
# int_board2 = convert_stringlist_to_intlist(read_test('./result2.txt'))
# testgenerator.generate_puzzle_from(int_board2,)

import test_generator2
test_generator2.generate_result()

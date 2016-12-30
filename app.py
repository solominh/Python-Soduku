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


import test_generator
import test_generator2
from sudoku_solver import SudkuSolver, print_result


test = test_generator2.generate_test()
result = SudkuSolver().get_one_solution(test)[0]
new_test = test_generator.generate_puzzle_from(result)

print_result(test)
print_result(result)
print_result(new_test)

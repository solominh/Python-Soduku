import random
from random import shuffle

from sudoku_solver import SudkuSolver
from sudoku_solver import print_result

posistion_list = [i for i in range(81)]
shuffle(posistion_list)


def generate_puzzle_from(result, removal_try=50):
    puzzle = result
    for index, pos in enumerate(posistion_list[:removal_try]):
        puzzle = try_remove_position(pos, puzzle)

    return puzzle


def try_remove_position(pos, puzzle):
    new_puzzle = puzzle[:pos] + [0] + puzzle[pos + 1:]  # Remove
    solver = SudkuSolver()
    if solver.check_more_than_one_solution(new_puzzle):
        return puzzle
    else:
        return new_puzzle



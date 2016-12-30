from random import shuffle
from sudoku_solver import SudkuSolver


posistion_list = [i for i in range(81)]
shuffle(posistion_list)
print(posistion_list)


def generate_puzzle_from(result):
    puzzle = result
    for index, pos in enumerate(posistion_list):
        puzzle = try_remove_position(pos, puzzle)

    print(puzzle)
    return puzzle


def try_remove_position(pos, puzzle):
    new_puzzle = puzzle[:pos] + [0] + puzzle[pos+1:]  #Remove
    solver = SudkuSolver()
    solution_count = solver.get_solution_count(new_puzzle)
    if solution_count == 1:
        return new_puzzle
    return puzzle

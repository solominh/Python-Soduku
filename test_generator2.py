from sudoku_solver import check_cell_valid, SudkuSolver, print_result
import random

empty_board = [0] * 81


def generate_test(min_cells_filled=27):
    try_fill_cells()
    while True:
        solver = SudkuSolver()
        result = solver.get_one_solution(empty_board)
        if result:
            return result
        else:
            try_fill_cells(1)


def try_fill_cells(numbers_of_cells_to_fill=27):
    try_cell_positions = set()
    count = 0

    while count < numbers_of_cells_to_fill:
        pos = random.randrange(81)
        if empty_board[pos] != 0 or pos in try_cell_positions:
            continue
        try_cell_positions.add(pos)

        number = try_fill_cell(pos)
        empty_board[pos] = number

        if number:
            count += 1


def try_fill_cell(pos):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    while numbers:
        number = random.choice(numbers)
        is_valid = check_cell_valid(pos, number, empty_board)
        if(is_valid):
            return number
        numbers.remove(number)
    return 0

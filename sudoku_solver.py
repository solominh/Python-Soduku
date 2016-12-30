
def print_result(board):
    print("Sudoku:\n")
    for i in range(9):
        print(board[i * 9:i * 9 + 9])
    print("\n")


def position_details(pos):
    row = pos // 9
    col = pos % 9
    block = row // 3 * 3 + col // 3
    return (row, col, block)


def check_cell_valid(pos, value, board):
    row, col, block = position_details(pos)
    start_cell_of_block = row // 3 * 3 * 9 + col // 3 * 3
    for i in range(9):
        rowi = row * 9 + i
        coli = col + i * 9
        blocki = start_cell_of_block + i % 3 + i // 3 * 9
        if value == board[rowi] or value == board[coli] or value == board[blocki]:
            return False

    return True


class SudkuSolver:

    def __init__(self):
        pass

    def get_one_solution(self, puzzle):
        self._solution_count = 0
        self._max_solution = 1
        self._run_backtrack(puzzle)
        return self._result if self._solution_count > 0 else None

    def check_more_than_one_solution(self, puzzle):
        self._solution_count = 0
        self._max_solution = 2
        self._run_backtrack(puzzle)
        return self._solution_count > 1

    def _run_backtrack(self, puzzle):
        self._row_flag = [[0] * 10 for _ in range(9)]
        self._col_flag = [[0] * 10 for _ in range(9)]
        self._block_flag = [[0] * 10 for _ in range(9)]
        self._puzzle = puzzle
        self._result = puzzle.copy()
        self._init_board_flags(self._puzzle)
        self._resolve_number_at(0)

    def _position_details(self, pos):
        row = pos // 9
        col = pos % 9
        block = row // 3 * 3 + col // 3
        return (row, col, block)

    def _init_board_flags(self, puzzle):
        for i, v in enumerate(puzzle):
            row, col, block = self._position_details(i)
            self._row_flag[row][v] = 1
            self._col_flag[col][v] = 1
            self._block_flag[block][v] = 1

    def _resolve_number_at(self, pos):
        if pos >= 81:
            self._solution_count += 1
            return self._solution_count >= self._max_solution

        if self._puzzle[pos] > 0:
            success = self._resolve_number_at(pos + 1)
            return success

        for num in range(1, 10):
            row, col, block = self._position_details(pos)
            if not (self._row_flag[row][num] or self._col_flag[col][num] or self._block_flag[block][num]):
                self._row_flag[row][num] = 1
                self._col_flag[col][num] = 1
                self._block_flag[block][num] = 1
                self._result[pos] = num
                success = self._resolve_number_at(pos + 1)
                if success:
                    return True
                self._row_flag[row][num] = 0
                self._col_flag[col][num] = 0
                self._block_flag[block][num] = 0
                self._result[pos] = 0

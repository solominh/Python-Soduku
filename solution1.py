def _print_board(board):
    print("Sudoku:\n")
    for i in range(9):
        print(board[i * 9:i * 9 + 9])
    print("\n")


def _position_details(pos):
    row = pos // 9
    col = pos % 9
    block = row // 3 * 3 + col // 3
    return (row, col, block)


def _resolve_number_at(pos):
    if pos >= 81:
        _print_board(output_board)
        return True

    if input_board[pos] > 0:
        success = _resolve_number_at(pos + 1)
        return success

    for num in range(1, 10):
        row, col, block = _position_details(pos)
        if not (row_flag[row][num] or col_flag[col][num] or block_flag[block][num]):
            row_flag[row][num] = 1
            col_flag[col][num] = 1
            block_flag[block][num] = 1
            output_board[pos] = num
            success = _resolve_number_at(pos + 1)
            if success:
                return True
            row_flag[row][num] = 0
            col_flag[col][num] = 0
            block_flag[block][num] = 0
            output_board[pos] = 0


def _init_board_flags(board):
    for i, v in enumerate(board):
        row, col, block = _position_details(i)
        row_flag[row][v] = 1
        col_flag[col][v] = 1
        block_flag[block][v] = 1


def solve(board):
    global row_flag, col_flag, block_flag, input_board, output_board

    row_flag = [[0] * 10 for _ in range(9)]
    col_flag = [[0] * 10 for _ in range(9)]
    block_flag = [[0] * 10 for _ in range(9)]
    input_board = board
    output_board = input_board.copy()

    _init_board_flags(output_board)
    _resolve_number_at(0)
    y = 1
    return output_board

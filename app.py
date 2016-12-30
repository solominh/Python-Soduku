

def create_region():
    region = [i // 3 * 3 + j // 3 for i in range(9) for j in range(9)]
    print_board(region)
    return region


def read_test():
    board = []
    with open('./test1.txt') as f:
        for line in f:
            board.extend([int(num) for num in line.strip()])

    print_board(board)
    return board


def write_result(board):
    with open('./result.txt', 'w') as f:
        for i in range(9):
            f.write(str(board[i * 9:i * 9 + 9]))
            f.write('\n')


def print_board(board):
    print("Sudoku:\n")
    for i in range(9):
        print(board[i * 9:i * 9 + 9])
    print("\n")


def position_details(pos):
    row = pos // 9
    col = pos % 9
    block = row // 3 * 3 + col // 3
    return (row, col, block)


def resolve_number_at(pos):
    if pos >= 81:
        print_board(board)
        write_result(board)
        exit()
        return

    if input_board[pos] > 0:
        resolve_number_at(pos + 1)
        return

    for num in range(1, 10):
        row, col, block = position_details(pos)
        if not (row_flag[row][num] or col_flag[col][num] or block_flag[block][num]):
            row_flag[row][num] = 1
            col_flag[col][num] = 1
            block_flag[block][num] = 1
            board[pos] = num
            resolve_number_at(pos + 1)
            row_flag[row][num] = 0
            col_flag[col][num] = 0
            block_flag[block][num] = 0
            board[pos] = 0


def init_board_flags(board):
    for i, v in enumerate(board):
        row, col, block = position_details(i)
        row_flag[row][v] = 1
        col_flag[col][v] = 1
        block_flag[block][v] = 1


row_flag = [[0] * 10 for _ in range(9)]
col_flag = [[0] * 10 for _ in range(9)]
block_flag = [[0] * 10 for _ in range(9)]
input_board = read_test()
board = input_board.copy()

init_board_flags(board)
resolve_number_at(0)

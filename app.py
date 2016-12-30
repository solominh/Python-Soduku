

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


def write_result():
    pass


def print_board(board):
    print("Sudoku:\n")
    for i in range(9):
        print(board[i * 9:i * 9 + 9])
    print("\n")


def resolve_number_at(pos):
    if pos >= 81:
        print_board(board)
        exit()
        return

    if input_board[pos] > 0:
        resolve_number_at(pos + 1)
        return

    for num in range(1,10):
        row = pos // 9
        col = pos % 9
        region = row // 3 * 3 + col // 3
        if not (row_flag[row][num] or col_flag[col][num] or region_flag[region][num]):
            row_flag[row][num] = 1
            col_flag[col][num] = 1
            region_flag[region][num] = 1
            board[pos] = num
            resolve_number_at(pos + 1)
            row_flag[row][num] = 0
            col_flag[col][num] = 0
            region_flag[region][num] = 0
            board[pos] = 0


def init_board_flags(board):
    for i, v in enumerate(board):
        row = i // 9
        col = i % 9
        region = row // 3 * 3 + col // 3

        row_flag[row][v] = 1
        col_flag[col][v] = 1
        region_flag[region][v] = 1


row_flag = [[0] * 10 for _ in range(9)]
col_flag = [[0] * 10 for _ in range(9)]
region_flag = [[0] * 10 for _ in range(9)]
input_board = read_test()
board = input_board.copy()

init_board_flags(board)
resolve_number_at(0)

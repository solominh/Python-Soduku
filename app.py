import solution1


def read_test():
    board = []
    with open('./test1.txt') as f:
        for line in f:
            board.extend([int(num) for num in line.strip()])
    return board


def write_result(board):
    with open('./result.txt', 'w') as f:
        for i in range(9):
            f.write(str(board[i * 9:i * 9 + 9]))
            f.write('\n')

board = solution1.solve(read_test())
write_result(board)

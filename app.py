import solution1
import solution2


def read_test():
    board = ''
    with open('./test1.txt') as f:
        for line in f:
            board += line.strip()
    return board


def write_result(board, filepath):
    with open(filepath, 'w') as f:
        for i in range(9):
            f.write(str(board[i * 9:i * 9 + 9]))
            f.write('\n')


def convert_stringlist_to_intlist(str_list):
    return list(map(int, str_list))


int_board = convert_stringlist_to_intlist(read_test())
board = solution1.solve(int_board)
write_result(board, './result.txt')


board2 = solution2.solve(read_test())
write_result(board2, './result2.txt')

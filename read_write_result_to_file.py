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

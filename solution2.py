def same_row(i, j): return (i // 9 == j // 9)


def same_col(i, j): return (i - j) % 9 == 0


def same_block(i, j): return (i // 27 == j // 27 and i % 9 // 3 == j % 9 // 3)


def resolve(a):
    i = a.find('0')
    if i == -1:
        print(a)
        return a

    excluded_numbers = set()
    for j in range(81):
        if same_row(i, j) or same_col(i, j) or same_block(i, j):
            excluded_numbers.add(a[j])

    for m in '123456789':
        if m not in excluded_numbers:
            result = resolve(a[:i] + m + a[i + 1:])
            if result:
                return result


def solve(board):
    return resolve(''.join(board))

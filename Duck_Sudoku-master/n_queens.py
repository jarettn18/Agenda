def queens(n):
    UNKNOWN = '.'
    QUEEN = 'Q'
    board = [[]]

    for i in range(len(n)):
        for j in range(len(n)):
            board.append(UNKNOWN)


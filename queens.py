def output_board(board):
    for row in board:
        print ' '.join(map(str, row))

num = 0

def place_queen(board, coordinate):
    new_board = []
    for row in board:
        new_board.append(row[:])
    x,y = coordinate

    for c in range(len(new_board)):
        new_board[x][c] = 1
        new_board[c][y] = 1

    dx, dy = x,y
    while not dx == 0 and not dy == 0:
        dx, dy = dx - 1, dy - 1
    while dx < len(new_board) and dy < len(new_board):
        new_board[dx][dy] = 1
        dx, dy = dx + 1, dy + 1

    dx, dy = x,y
    while dy != 0 and dx != len(new_board) - 1:
        dx, dy = dx + 1, dy - 1
    while dx > 0 and dy < len(new_board):
        new_board[dx][dy] = 1
        dx, dy = dx - 1, dy + 1

    return new_board

def produce_board(n):
    res = []
    for _ in range(n):
        res.append([0]*n)
    return res

def n_queens(board, x):
    global num
    n = len(board)
    if n - 1 == x:
        return sum(map(lambda x: 1 if x == 0 else 0, board[x]))
    s = 0
    for y in range(n):
        num += 1
        if board[x][y] == 0:
            s += n_queens(place_queen(board, (x,y)), x+1)
    return s
        
n_queens(produce_board(8), 0)
print num

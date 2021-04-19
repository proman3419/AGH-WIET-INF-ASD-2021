import random

print("hello!")

def puotki(A,k):
    n = len(A)
    T = [ [-1]*n for i in range(k+1) ]

    def f(i, j, A):
        if T[i][j] >= 0: # TABLICA
            return T[i][j]
        if i == 0:
            T[i][j] = 0 # TABLICA
            return 0
        if i == 1:
            summ = 0
            for s in range(j + 1):
                summ += A[s]
            T[i][j] = summ # TABLICA
            return summ

        max_now = 0
        for p in range(j):
            summ = 0
            for l in range(p, j + 1):
                summ += A[l]
            fval = f(i - 1, p-1, A) # TU BYŁO    fval = f(i - 1, p, A)
            min_local = min(fval, summ)
            max_now = max(max_now, min_local)
        T[i][j] = max_now # TABLICA
        return max_now

    return f(k,n-1,A)


def chessboard(board):
    n = len(board)
    helper_board = [[0 for _ in range(n)] for _ in range(n)]
    helper_board[0][0] = board[0][0]

    for y in range(n):
        for x in range(n):
            if x == 0:
                helper_board[y][x] = helper_board[y-1][x] + board[y][x]
            elif y == 0:
                helper_board[y][x] = helper_board[y][x-1] + board[y][x]

            else:
                helper_board[y][x] = min(helper_board[y-1][x], helper_board[y][x-1]) + board[y][x]

    print(helper_board[n-1][n-1])

chess = [[random.randint(1, 10) for _ in range(4)] for _ in range(4)]
chessboard(chess)
for lane in chess:
    print(lane)

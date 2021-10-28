h, w = map(int, input().split())
board = [[0 for i in range(w)] for j in range(h)]
for _ in range(int(input())):
    l, d, x, y = map(int, input().split())
    x -= 1; y -= 1
    if d == 0:
        for i in range(l): board[x][y + i] = 1
    else:
        for i in range(l): board[x + i][y] = 1
for i in range(h):
    for j in range(w):
        print(board[i][j], end=' ')
    print()
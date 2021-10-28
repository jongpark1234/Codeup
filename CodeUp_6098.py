antcave = []
x, y = 1, 1
for i in range(10):
    antcave.append(list(map(int, input().split())))
while True:
    if antcave[x][y + 1] != 1:
        antcave[x][y] = 9; y += 1
        if antcave[x][y] == 2:
            antcave[x][y] = 9; break
    elif antcave[x + 1][y] != 1:
        antcave[x][y] = 9; x += 1
        if antcave[x][y] == 2:
            antcave[x][y] = 9; break
    else:
        antcave[x][y] = 9; break
for i in range(10):
    for j in range(10):
        print(antcave[i][j], end=' ')
    print()
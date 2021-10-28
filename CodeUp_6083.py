import sys
r, g, b = map(int, sys.stdin.readline().split()); times = 0
for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i, j, k); times += 1
print(times)
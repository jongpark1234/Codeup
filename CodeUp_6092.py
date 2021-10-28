n = int(input()); slist = list(map(int, input().split())); called = [0] * 23
for i in slist: called[i - 1] += 1
for i in called: print(i, end=' ')
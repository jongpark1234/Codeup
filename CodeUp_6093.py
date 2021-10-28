n = int(input())
slist = list(map(int, input().split()))
slist.reverse()
for i in range(n): print(slist[i], end=' ')
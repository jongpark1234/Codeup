day = 1
a, b, c = map(int, input().split())
while not(day % a == 0 and day % b == 0 and day % c == 0): day +=  1
print(day)
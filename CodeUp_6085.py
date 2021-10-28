w, h, b = map(int, input().split())
print('{:.2f} MB'.format(round(w * h * b / 8 / (1024 ** 2), 2)))
a = int(input(), 16)
for i in range(1, 16): print(f'{hex(a)[2:]}*{hex(i)[2:]}={hex(a * i)[2:]}'.upper())
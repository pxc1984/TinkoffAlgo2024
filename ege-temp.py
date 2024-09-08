from itertools import product

cnt = 0
for i in product(sorted(["А", "В", "Т", "О", "П"]), repeat=4):
    cnt += 1
    if ''.join(i) == 'ВАТА':
        print(cnt, i)

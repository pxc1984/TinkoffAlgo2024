from itertools import product

cnt = 0
for i in product(["К", "Л", "Р", "Т"], repeat=4):
    cnt += 1
    if cnt == 67:
        print(cnt, i)
        break

from itertools import product

cnt = 0
for i in product(["А", "О", "У"], repeat=5):
    cnt += 1
    if i[0] == "О":
        print(cnt, i)
        break

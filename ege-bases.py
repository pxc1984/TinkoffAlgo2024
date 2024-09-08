import string

digs = string.digits + string.ascii_letters


def int2base(x, base):
    if x < 0:
        sign = -1
    elif x == 0:
        return digs[0]
    else:
        sign = 1

    x *= sign
    digits = []

    while x:
        digits.append(digs[x % base])
        x = x // base

    if sign < 0:
        digits.append('-')

    digits.reverse()

    return ''.join(digits)


# print(bin(int("12F0", base=16)).count('1'))

# for i in range(8, 12):
#     print(i, bin(i), bin(i).count('1'))

# print(int("10101010", base=2) - int("252", base=8) + int("7", base=16))

# for i in [1, 3, 11, 33]:
#     cnt = bin(i).count('1')
#     if cnt == 3:
#         print(i)

# max_n = 0
# num = 0
# for i in [int("B8", base=16), int("176", base=8), int("10011011", base=2)]:
#     cnt = bin(i).count('1')
#     if max_n < cnt:
#         max_n = cnt
#         num = i
#
# print(max_n, num, bin(num))

# a = int("AB", base=16)
# b = int("311", base=8)
# print(b - a)
# cnt = 0
# for i in range(a, b):
#     print(i)
#     cnt += 1
# print(cnt)

# cnt = 0
# cnt += int("10011010", base=2) > 256
# cnt += int("10011010", base=2) > int("9F", base=16)
# cnt += int("10011010", base=2) > int("232", base=8)
# print(cnt)

# cnt = 0
# n = int("A4", base=16) + int("20", base=8)
# for i in ["10001011", "10111000", "10011011", "10110100"]:
#     cnt += int(i, base=2) > n
# print(cnt)

for i in range(int("1000", base=8), int("10000", base=8)):
    if bin(i).count('0') == 6:
        print(int2base(i, 8), i, bin(i))
        break

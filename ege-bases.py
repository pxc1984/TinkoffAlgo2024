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


expression_value = 7 * 512 ** 120 - 6 * 64 ** 100 + 8 ** 210 - 255
to_base = int2base(expression_value, 8)
ones_count = to_base.count('0')
print(to_base)  # может иметь смысл это закомментировать

print(ones_count)

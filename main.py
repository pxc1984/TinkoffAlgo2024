k, x, n = map(int, input().split())

# ширина - k^n * x
# высота - k ^ (n-1) * x + 1

maxX, maxY = 1, 1

if n == 1:
    print("#" * x)
    maxX = x
    maxY = 1
if n == 2:

    print()


print(f"\n{maxX} {maxY}")

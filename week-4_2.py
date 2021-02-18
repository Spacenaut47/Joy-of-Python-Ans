m = int(input())
n = int(input())
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
ans = 0
if m + n >= 20:
    print('invalid', end="")
else:
    numerator = (m + 1) * (factorial(m) ** 2)
    denominator = factorial(m - n + 1)
    print(int(numerator / denominator), end="")

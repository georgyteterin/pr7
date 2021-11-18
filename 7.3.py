def power(a, n):
    if n == 1:
        return a
    if n % 2 != 0:
        return a * power(a, n - 1)
    else:
        return power(a, n / 2) ** 2
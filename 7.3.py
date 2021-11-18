a=int(input("enter the base: ", ))
n=int(input("enter the the exponent or power: ", ))

def power(a, n):
    if n == 0 and a == 0:
        return "oops we can't do it"
    if n == 0 and a != 0:
        return 1
    if n == 1:
        return a
    if n % 2 != 0:
        return a * power(a, n - 1)
    else:
        return power(a, n / 2) ** 2

print(power(a, n))
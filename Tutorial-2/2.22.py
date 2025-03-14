
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

def nCr(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

print(nCr(5, 2))

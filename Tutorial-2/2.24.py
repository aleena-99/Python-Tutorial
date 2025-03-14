mport math

def sin_x(x, n):
    result = 0
    for i in range(n):
        term = ((-1) * i) * (x * (2 * i + 1)) / math.factorial(2 * i + 1)
        result += term
    return result

print(sin_x(math.radians(30), 10))

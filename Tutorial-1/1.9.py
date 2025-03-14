x, y = map(int, input("Enter X and Y: ").split())
result = 1
for _ in range(abs(y)):
    result *= x
print(result if y >= 0 else 1/result)

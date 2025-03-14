n = int(input("Enter a number: "))
print(f"Sum of cubes: {sum(i**3 for i in range(2, n+1, 2))}")

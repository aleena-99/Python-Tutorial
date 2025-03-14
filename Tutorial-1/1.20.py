l, u = map(int, input("Enter lower and upper limit: ").split())
print(f"Sum of odd numbers: {sum(range(l | 1, u + 1, 2))}")

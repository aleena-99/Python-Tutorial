nums = list(map(int, input("Enter numbers: ").split()))
print(f"Sum of even numbers: {sum(n for n in nums if n % 2 == 0)}")

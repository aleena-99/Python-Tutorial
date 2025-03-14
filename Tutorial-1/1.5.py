nums = list(map(int, input("Enter numbers: ").split()))
evens = sum(1 for n in nums if n % 2 == 0)
print(f"Evens: {evens}, Odds: {len(nums) - evens}")

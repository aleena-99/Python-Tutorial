nnums = [int(input("Enter number: ")) for _ in range(4)]

pos = [n for n in nums if n > 0]
neg = [n for n in nums if n < 0]

print(f"Sum of positives: {sum(pos)}, Average: {sum(pos)/len(pos) if pos else 0}")
print(f"Sum of negatives: {sum(neg)}, Average: {sum(neg)/len(neg) if neg else 0}")

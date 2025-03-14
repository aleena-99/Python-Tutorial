
from collections import Counter

def find_mode(numbers):
    freq = Counter(numbers)
    return max(freq, key=freq.get)

print(find_mode([1, 2, 2, 3, 3, 3, 4, 5]))

def find_median(numbers):
    numbers.sort()
    n = len(numbers)
    mid = n // 2
    return (numbers[mid] if n % 2 != 0 else (numbers[mid - 1] + numbers[mid]) / 2)

print(find_median([5, 3, 8, 1, 2]))

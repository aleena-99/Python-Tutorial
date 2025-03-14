def sum_even(numbers):
    return sum(n for n in numbers if n % 2 == 0)

print(sum_even([1, 2, 3, 4, 5, 6]))

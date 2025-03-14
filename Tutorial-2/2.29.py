def sum_of_evens():
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    print("Sum of even numbers:", sum(n for n in numbers if n % 2 == 0))

sum_of_evens()

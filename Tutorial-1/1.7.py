num = int(input("Enter a number: "))
i = 2
while num > 1:
    while num % i == 0:
        print(i, end=" ")
        num //= i
    i += 1

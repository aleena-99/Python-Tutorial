num = input("Enter a number: ")
print("Armstrong" if sum(int(digit)**len(num) for digit in num) == int(num) else "Not Armstrong")

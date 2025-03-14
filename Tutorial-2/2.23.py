def menu():
    while True:
        print("1. Check even or odd")
        print("2. Check number sign")
        print("3. Generate factors")
        print("4. Exit")
        choice = int(input("Enter choice: "))
        
        if choice == 1:
            num = int(input("Enter number: "))
            print("Even" if num % 2 == 0 else "Odd")
        elif choice == 2:
            num = int(input("Enter number: "))
            print("Positive" if num > 0 else "Negative" if num < 0 else "Zero")
        elif choice == 3:
            num = int(input("Enter number: "))
            print([i for i in range(1, num + 1) if num % i == 0])
        elif choice == 4:
            break

menu()

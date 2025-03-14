print([n for n in range(2, 1000) if all(n % i != 0 for i in range(2, int(n**0.5) + 1))])

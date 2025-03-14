print([n for n in range(100, 1001) if sum(map(int, str(n))) % 9 == 0])

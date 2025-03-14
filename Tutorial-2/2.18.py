def reverse_halves(s):
    mid = len(s) // 2
    return s[:mid][::-1] + s[mid:][::-1]

print(reverse_halves("HelloWorld"))

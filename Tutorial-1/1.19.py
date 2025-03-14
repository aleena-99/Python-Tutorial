a, b, c = map(float, input("Enter a, b, c: ").split())
d = b**2 - 4*a*c

if d >= 0:
    print(f"Roots: {(-b + d*0.5) / (2*a):.2f}, {(-b - d*0.5) / (2*a):.2f}")
else:
    print("Complex roots")

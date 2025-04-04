x, y = map(float, input("Enter x and y coordinates: ").split())

if x > 0 and y > 0:
    print("Quadrant I")
elif x < 0 and y > 0:
    print("Quadrant II")
elif x < 0 and y < 0:
    print("Quadrant III")
elif x > 0 and y < 0:
    print("Quadrant IV")
else:
    print("Point lies on an axis or at origin")

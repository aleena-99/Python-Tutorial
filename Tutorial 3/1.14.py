import turtle

t = turtle.Turtle()
t.speed(0)

for _ in range(10):
    for _ in range(6):
        t.forward(50)
        t.right(60)
    t.right(36)

turtle.done()

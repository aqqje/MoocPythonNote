import turtle as t
def koch(size, n):
    if n == 0:
        t.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
            t.left(angle)
            koch(size / 3, n - 1)

def main():
    t.setup(800, 400)
    t.penup()
    t.goto(-200, 150)
    t.pendown()
    t.pensize(2)
    level = 3
    koch(600, level)
    t.right(120)
    koch(600, level)
    t.right(120)
    koch(600, level)
    t.hideturtle()
    t.done()

main()
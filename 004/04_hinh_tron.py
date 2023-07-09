import turtle
def ve_hinh_tron(r):
    t.circle(r)
    return 3.14*r**2


bk = float(input())

t = turtle.Turtle()
print(ve_hinh_tron(bk))

turtle.done()
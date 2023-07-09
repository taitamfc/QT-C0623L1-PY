import turtle
t=turtle.Turtle()
def hinhvuong(a):
    for i in range (1,5):
        t.forward(a)
        t.right(90)
step=36
angle=360/step
for j in range (1,int(angle+1)*2):
    hinhvuong(100)
    t.right(step/2)
turtle.done()

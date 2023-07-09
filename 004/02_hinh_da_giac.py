import turtle
t=turtle.Turtle()
t.hideturtle()
t.pencolor('red')
def drawn(n,chieu_dai):
    angle=(n-2)*180/n
    for i in range(n):
        t.forward(chieu_dai)
        t.right(180-angle)
drawn(6, 150)
turtle.done()       

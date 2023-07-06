import turtle

t = turtle.Turtle()

#vẽ tường nhà
t.color("gray")
t.begin_fill()
t.forward(200)
t.right(90)
t.forward(150)
t.right(90)
t.forward(200)
t.right(90)
t.forward(150)
t.end_fill()

#vẽ mái nhà
t.penup()
t.goto(-50, 150)
t.pendown()
t.color("red")
t.begin_fill()
t.forward(300)
t.left(120)
t.forward(200)
t.left(120)
t.forward(200)
t.end_fill()

#vẽ cửa nhà
t.penup()
t.goto(50,0)
t.pendown()
t.color("brown")
t.begin_fill()
t.forward(40)
t.right(90)
t.forward(70)
t.right(90)
t.forward(40)
t.right(90)
t.forward(70)
t.end_fill()

#vẽ cửa sổ nhà
t.penup()
t.goto(125,75)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(25)
t.end_fill()

tuple.done()
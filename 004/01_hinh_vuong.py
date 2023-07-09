# nhúng thư viện vào
import turtle

# tạo đối tượng
t = turtle.Turtle()
t.hideturtle()
t.pencolor('black')

# xây dựng hàm
def hinh_vuong(n):
    for i in range(4):
        t.forward(n)
        t.right(90)

    turtle.done()

# gọi hàm
hinh_vuong(100)
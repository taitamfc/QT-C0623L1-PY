# Bước 1: Nhúng thư viện vào
import turtle
# Bước 2: tạo đối tượng
t = turtle.Turtle()

t.color("green")
t.begin_fill()
#Vẽ ngang (tiến về trước 100px)
t.forward(100)

#Quay phải 90 độ
t.right(90)

#Vẽ dọc từ trên xuống dưới (tiến về trước 100px)
t.forward(100)

#Quay phải 90 độ
t.right(90)

#Vẽ ngang từ trái sang phải (tiến về trước 100px)
t.forward(100)

#Quay phải 90 độ
t.right(90)

#Vẽ từ dưới lên trên (tiến về trước 100px)
t.forward(100)
t.end_fill()

#Kết thúc
turtle.done()

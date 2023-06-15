# Bước 1: Nhúng thư viện vào
import turtle
# Bước 2: tạo đối tượng
t = turtle.Turtle()

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

#Dừng vẽ
t.penup()

#Quay trái 90 độ
t.left(90)

#Chạy sang trái 100px
t.forward(100)

#Đặt bút vẽ xuống
turtle.pendown()

#Thiết lập màu sắc
t.color('red')

#Bắt đầu tô màu
t.begin_fill()

#Vẽ từ phải sang trái 100px
t.forward(100)

#Quay trái 90 độ
t.left(90)

#Vẽ từ trên xuống dưới 100px
t.forward(100)

#Quay trái 90 độ
t.left(90)

#Vẽ từ trái sang phải 100px
t.forward(100)

#Quay trái 90 độ
t.left(90)

#Vẽ từ dưới lên trên 100px
t.forward(100)

#Kết thúc tô màu
t.end_fill()


#Kết thúc
turtle.done()

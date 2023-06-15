# Bước 1: Nhúng thư viện vào
import turtle
# Bước 2: tạo đối tượng
t = turtle.Turtle()
# Bước 3: Các lệnh điều khiển

# Di chuyển về phía trước với khoảng cách 100px
turtle.forward(100)

# Rẻ phải một góc 90 độ
turtle.right(90)

# Di chuyển về phía sau với khoảng cách 100px
turtle.backward(100)

# Rẻ trái một góc 90 độ
turtle.left(90)

#Dừng vẽ khi di chuyển turtle
turtle.penup()

#Bắt đầu vẽ khi di chuyển turtle
turtle.pendown()

#Thay đổi kích thước của bút vẽ của turtle theo giá trị size
turtle.pensize(10)

#Kết thúc
turtle.done()

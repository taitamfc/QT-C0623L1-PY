import turtle
import math

# Khởi tạo turtle và màn hình vẽ
screen = turtle.Screen()
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(0)  # Đặt tốc độ nhanh nhất

# Khởi tạo các biến
a = 100  # Bán kính theo trục x
b = 50   # Bán kính theo trục y
angle = 0  # Góc ban đầu

# Vẽ hình ellipse trong vòng lặp while
while angle < 360:
    # Thiết lập màu sắc cho bút vẽ
    t.pencolor("blue")

    # Tính toán tọa độ x và y của điểm trên ellipse
    x = a * math.cos(math.radians(angle))
    y = b * math.sin(math.radians(angle))

    # Di chuyển turtle đến tọa độ (x, y)
    t.goto(x, y)

    # Thay đổi góc quay
    angle += 1

# Đóng cửa sổ đồ hoạ turtle khi hoàn thành
turtle.done()

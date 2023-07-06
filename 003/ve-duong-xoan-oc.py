import turtle

t = turtle.Turtle()
t.speed(0)  # Đặt tốc độ nhanh nhất

# Khởi tạo các biến
d = 1
initial_point = t.position()

# Vẽ đường xoắn ốc tròn
while True:
    # Tiến về phía trước 1 khoảng d
    t.forward(d)
    
    # Xoắn ngược chiều kim đồng hồ
    t.right(10)  # Thay đổi góc xoắn thành 10 độ (hoặc giá trị khác tùy ý)
    
    # Tăng d lên một chút
    d += 0.1
    
    # Tính khoảng cách từ điểm hiện tại đến điểm ban đầu
    distance = t.distance(initial_point)
    
    # Kiểm tra điều kiện thoát khỏi vòng lặp
    if distance > 200:
        break

# Đóng cửa sổ đồ hoạ turtle khi hoàn thành
turtle.done()

# Bước 1: Dùng for…in và range(1, 10) để tạo vòng lặp, 
# biến số của vòng lặp tượng cho cho bảng cửu chương của số sắp sửa được in.
for number in range(1, 10):
    print(f"Bảng cửu chương {number}:")

    # Bước 2: Trong mỗi vòng lặp trên, tiếp tục sử dụng for…in và hàm range(1, 10) để bắt đầu tính 
    for i in range(1, 10):
        # và in ra tích của number và các số từ 1 đến 9.
        result = number * i
        print(f"{number} x {i} = {result}")
    print()

# Bước 1: Cho người dùng nhập biến

#Dùng hàm input() để nhập hai số bất kì
range_input = input("Nhập khoảng (cú pháp: start-end): ")
# Dùng hàm split() để tách chuỗi số vừa nhập để lấy được số bất đầu và số kết thúc.
range_input = range_input.split('-')

# Lấy số bắt đầu và kết thúc
start = range_input[0]
end  = range_input[1]
# Dùng hàm int() để chuyển số bắt đầu và kết thúc về kiểu int.
start = int(start)
end = int(end)

# Bước 2: Kiểm tra biến nhập

# Nếu số kết thúc bé hơn số bắt đầu thì thông báo số kết thúc cần lớn hơn số bắt đầu
if end < start:
    print("Số kết thúc cần lớn hơn số bắt đầu.")
else:
    # Bước 3: Bắt đầu xử lý việc in kết quả

    # Dùng for…in range(start, end) để khởi tạo vòng lặp
    for num in range(start, end + 1):
        # Trong mỗi vòng lặp sẽ dùng khổi lệnh if…elif…else để kiểm tra biến lặp và in ra kết quả phù hợp: 

        # Chia hết cho 3 và 5 thì in ra “FizzBuzz”
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")

        # Hoặc chia hết cho 3 thì in ra “Fizz”
        elif num % 3 == 0:
            print("Fizz")

        # Hoặc chia hết cho 5 thì in ra “Buzz”
        elif num % 5 == 0:
            print("Buzz")

        # Không thuộc 3 trường hợp trên thì ra chính giá trị của biến lặp
        else:
            print(num)

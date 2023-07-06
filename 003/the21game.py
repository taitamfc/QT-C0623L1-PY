import random

# Bước 1: Khởi tạo vòng lặp
while(True):
    # Bước 2: Sử lý trong vòng lặp
    # Bước 2.1
    current_number = 0

    # Bước 2.2:
    if ( random.randint(0, 1) == 0):
        current_player  = 'human'
    else:
        current_player  = 'computer'

    # Bước 2.3:
    while (current_number <= 21):
        # In ra giá trị current_number cho người dùng
        print("Số hiện tại: " + str(current_number))

        # Dùng if…else để bắt đầu kiểm tra lượt chơi:

        # Nếu là lượt chơi của người
        if (current_player == 'human'):
            # Khai báo biến player_choice mang giá trị khởi tạo là chuỗi rỗng
            player_choice = ''
            # Dùng while để tạo vòng lặp kiểm tra giá trị player_choice có thuộc danh sách [‘1’, ‘2’, ‘3’] hay không
            while player_choice not in ['1', '2', '3']:
                player_choice = input("Nhập vào 1, 2, hoặc 3: ")

            # Dùng hàm int() để chuyển biến player_choice sang kiểu int
            player_choice = int(player_choice)

            # Giá trị current_number hiện tại sẽ được cộng thêm player_choice
            current_number = current_number + player_choice

            # Dùng hàm if để kiểm tra giá trị của current_number đã lớn hơn hoặc bằng 21 chưa:
            if (current_number >= 21):
                # Nếu đúng thì in ra số hiện tại.
                print("Số hiện tại: " + str(current_number) )
                #thông báo rằng người dùng đã thua
                print("Bạn đã thua")
                #kết thúc vòng lập
                break
            else:
                # Nếu sai thì gán giá trị mới cho current_player = ‘computer’ => lượt chơi tiếp theo sẽ là máy.
                current_player = 'computer'

        # Nếu là lượt chơi của máy
        if (current_player == 'computer'):
            # Khai báo biến computer_choice, mang giá trị số mà máy sẽ chọn 
            computer_choice = random.randint(1, 3)
            # In computer_choice ra để thông báo cho người chơi biết.
            print("Máy tính đã chọn:" + str(computer_choice) )
            # Giá trị current_number lúc này sẽ được cộng thêm computer_choice.
            current_number = current_number + computer_choice

            # Dùng hàm if để kiểm tra giá trị của current_number đã lớn hơn hoặc bằng 21 chưa: 
            if current_number >= 21:
                # Nếu đúng thì in ra số hiện tại, thông báo rằng người chơi đã thắng và kết thúc vòng lập. 
                print("Số hiện tại: " + str(current_number))
                # thông báo rằng người chơi đã thắng
                print("Bạn đã thắng !")
                #kết thúc vòng lập
                break
            else:
                # Nếu sai thì thì gán giá trị mới cho current_player = ‘human’ => lượt chơi tiếp theo sẽ là người dùng.
                current_player = 'human'
    
    # Bước 3: Khi vòng lặp kết thúc, Dùng input() để hỏi người chơi có muốn chơi lại không và gán giá trị cho biến play_again
    play_again = input("Bạn có muốn chơi lại hay không ? ")
    
    # Bước 4: Dùng if…else để kiểm tra giá trị play_again:
    # Nếu play_again bắt đầu bằng “y” thì dùng continue cho vòng lặp tiếp tục
    if play_again.lower().startswith('y'):
        continue
    else:
        break

'''
Cho một số nguyên n, hãy thực hiện các hành động có điều kiện sau:

Nếu n là số lẻ, hãy in Weird
Nếu n là số chẵn và nằm trong phạm vi bao gồm từ 2 đến 5, hãy in Not Weird
Nếu n là số chẵn và nằm trong phạm vi bao gồm từ 6 đến 20, hãy in Weird
Nếu n là số chẵn và lớn hơn 20, hãy in Not Weird
Định dạng đầu vào

Một dòng chứa một số nguyên dương, n.

Ràng buộc
1<= n <=100
Định dạng đầu ra

In Weird nếu số đó là số lẻ. Nếu không, hãy in Not Weird.

Đầu vào mẫu 0
3

Đầu ra mẫu 0
Weird

Giải thích 0
n = 3
n là số lẻ và số lẻ là số lẻ, vì vậy hãy in Weird.

Đầu vào mẫu 1
24

Đầu ra mẫu 1
Not Weird

Giải thích 1

n=24
n >20 và là số chẵn, vì vậy nó không phải là số lẻ.
'''
n = int(input("n = "))

if range(0,101):
    if n % 2 != 0:
        print("Weird")
    elif n % 2 == 0 and 2 <= n <= 5:
        print("Not Weird")
    elif n % 2 == 0 and 6 <= n <= 20:
        print("Weird")
    elif n % 2 == 0 and n > 20:
        print("Not Weird")
else:
    print("Giá trị n phải nằm trong khoảng từ 1 đến 100. Vui lòng nhập lại.")
    

n = int(input(""))

if range(0,101):
    if n % 2 != 0:
        print("Weird")
    elif n % 2 == 0 and n in range(1,6):
        print("Not Weird")
    elif n % 2 == 0 and n in range(5,21):
        print("Weird")
    elif n % 2 == 0 and n > 20:
        print("Not Weird")
else:
    print("khong thuoc trong pham vi 1 - 100 yeu cau nhap lai")

    

        
    
        
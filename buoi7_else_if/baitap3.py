#Nhập hai số a và b từ bàn phím. In ra số lớn nhất và nhỏ nhất trong hai số

a = float(input("nhập số a:"))
b = float(input("nhập số b:"))

if a>b:
    print("số lớn nhất là ",a)
elif a<b:
    print("số lớn nhất là:",b)
else:
    print("hai số bằng nhau")
    
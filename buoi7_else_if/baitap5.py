#Giải và biện luận phương trình bậc hai 1 ẩn ax^2 + bx + c = 0 (ẩn x, a, b, c là ba số cho trước)
import math
a = float(input("Nhập số a cho phương trình bậc 2:"))
b = float(input("Nhập số b cho phương trình bậc 2:"))
c = float(input("Nhập số c cho phương trình bậc 2:"))

delta = b**2 - 4*a*c
x = -b/2*a
x1=(-b + math.sqrt(delta))/2*a
x2=(-b - math.sqrt(delta))/2*a

if delta > 0:
    print(f"Phương trình có 2 nghiệm phân biệt:","\nx1 là:{x1}","\n x1 là:{x2}")
elif delta == 0:
    print("Phương trình có nghiệm kép :",x)
else:
    print("phương trình không có nghiệm thực")
    
#Giải và biện luận phương trình bậc nhất một ẩn ax + b = 0 (ẩn x, a và b là hai số cho trước)
# làm cachs nào khi nhập một số nguyên sẽ về dạng 5x+6 =0 chứ không phải 5.0x + 6.0 =0

a = float(input("Nhập số a vào phương trình:"))
b = float(input("Nhập số b vào phương trình:"))

print(f"Phương trình có dạng {a}x + {b} =0")
x= -b/a
if a ==0: 
    if b !=0 :
        print("phương trình vô nghiệm")
    else :
        print("phương trình có vô số nghiệm")
else:
    print("Phương trình có nghiệm là:",x)
    
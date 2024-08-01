#Nhập vào một số nguyên dương n. Đếm số lượng số chẵn và lẻ trong đoạn [0, n]
even = 0
ode =0

n = int(input("Nhap vao mot so nguyen dương cho chuỗi:"))
while n <=0 :
    print("Cần nhập vào là một số nguyên dương")
    n = int(input("Nhap vao mot so nguyen dương cho chuỗi:"))
for i in range(n+1):
    if i%2==0:
        even +=1
        
    else:
        ode +=1
        
print("Tổng số chẵn là : ",even)
print("Tổng số lẻ là",ode)
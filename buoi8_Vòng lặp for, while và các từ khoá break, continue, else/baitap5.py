
# 5. Nhập vào một số nguyên dương n tính tổng các chữ số của n. Ví dụ: n = 4312 => S = 4 + 3 + 1 + 2 = 10
n = int(input("n = "))

while n <= 0:
    print("n phải là số nguyên dương")
    n = int(input("n = "))
    
S = 0

while n > 0:
    last = n % 10
    S += last
    n //= 10
    
print(S)




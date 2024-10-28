'''
Đoạn mã được cung cấp đọc và số nguyên, n, từ STDIN. Đối với tất cả các số nguyên không âm i < n, in i^2.

Ví dụ
n = 3
Danh sách các số nguyên không âm nhỏ hơn n = 3 là [0,1,2] . In bình phương của mỗi số trên một dòng riêng biệt.

0
1
4
Định dạng đầu vào

Dòng đầu tiên và duy nhất chứa số nguyên, n.

Ràng buộc
1 <= n <=20

Định dạng đầu ra

In n dòng, mỗi dòng tương ứng với i.

Đầu vào mẫu 0

5
Đầu ra mẫu 0

0
1
4
9
16
'''

n = int(input())
if n in  range(0,21):
    for i in range(0,n):
        print(i **2)
else:
    print("Vui long nhap lai")
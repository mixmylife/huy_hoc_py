'''
+ Set
set là một cấu trúc dữ liệu không cho phép các phần tử trùng lặp, không có thứ tự cố định, không thể truy cập bằng chỉ số
set được tạo sử dụng cặp dấu ngoặc nhọn, nếu trống thì nó là dict trống không phải set
tạo một set trống thì sử dụng như sau: set()
set k có thứ tự k chứa giá trị trùng lặp 


+ tuple
Tuple (Bộ giá trị)
tuple được sử dụng để lưu trữ nhiều giá trị trong một biến duy nhất
tuple là một cấu trúc dữ liệu có thứ tự, cho phép các giá trị trùng lặp
tuple bản thân nó và các phần tử bên trong nó không thể thay đổi
tuple được tạo bởi cặp dấu ngoặc tròn (nên dùng) ngăn cách với nhau bằng dấu phẩy (,)
tuple cũng giống như list truy cập vào các phần tử bằng chỉ số (index)
k có thứ tự k chứa giá trị trùng lặp 
'''

#tuple 
#thường dùng trong csdl

# tup1 = 1,2,3
# print(type(tup1))
# tup2 = (1,2,3)
# print(type(tup2))
# tup3 = 1,
# print(type(tup3))
# tup4 = (4,)
# print(type(tup4))
# huy = (4,9)
# print(type(huy))


# print(tup1[0])
# print(tup1[-1])

# # tup1[0] =1000
# # tup1[2] =1000

# # tup1.append(1000)

# tup1 +=(4,)
# print(tup1)
# tup1 +=(4,5,6,8,9,5,6,4,2,5)
# print(tup1)


# #set
# set1 = set()
# print(len(set1))

# set1.add(1)
# set1.add(1)
# set1.add(1)
# set1.add(1)
# set1.add(1)
# print(set1)

# set1.update(2,44,5,63,1,6)
# print(set1)

# set1.remove(1)
# set2 = set1.copy()
# print(set1 is set2)
# print(set1 == set2)

# # so sanh 2 hay nhieu truong hop de tim dac diem trung
# # check trùng giá trị

# set1.clear()
# print(set1)

# set2 = {1,4,34,43,5,3,6}
# print(set2)
# # set2.add([1,2,5,4,3])
# set2.add("HUYDuyen")
# print(set2)

# # print(set[-1] ) không thể truy cấp các phần tử bằng dấu ngoặc vuông

# set2.remove(1000)


# set3 = set()
# set3.pop()
# set3 ={2,9,8,5,3,6,25,98,115,6645}
# any_value = set3.pop()
# print(any_value)
# print(set3)

# set = {}  #kiểu dict

# # terminal
# #  ktra phiên bản python đang dùng: python -v
# # ktra trên mấy có bao nhiêu phiên bản python đc cài đặt: python -0p
# # cài thư viện : python -m venv venv

# # cmd 
# # để xem python đang dùng nằm ở đâu : where python


# t = 4, 5 
# a, b = t
# print(a)


# # a, b, c= 4,6,5
# # print(c)


# # list chứa tuple
# friends = [
#     ("Bob",23),
#     ("huy",34),
#     ("duyen",22)
# ]

# print(friends[0][1])
# print(friends[-1])
# print(friends[2])


lst = [[1,[2,3]],(2,4)]
# lấy [2,3]
print(lst[0][-1])
print(lst[0][1])

# lấy 2 trong [2,3]
print(lst[0][-1][0])

#lấy (2,4)
print(lst[1])

#lấy 1
print(lst[0][0])

lst[0][1].append(100)
print(lst)
#
lst.append(100)
print(lst)

#copy
lst1 = lst.copy() #hoặc lst[:]

#copy lisst ma khong co so 100
from copy import deepcopy
lst =deepcopy(lst)

#kiem tra xem doi tuong nay co phai la kieu nay hay khong
print(isinstance(3,int))
print(isinstance(3,float))
print(isinstance(0j,complex))
print(isinstance(True,int))

#khi truyen vao khi tu se in ta ma so cua no
print(ord('a'))
print(ord('a') ^ ord('3')) #XOR
#print(ord('ab')) #RA LOI chi dc truyen vao 1 ki tu duy nhat

# ham gia tri tuyet doi
print(abs(True))
print(abs(-True))

print(abs('a')) #looix chi cho dung voi 1 so
print(abs('1+2j')) # ra can bac 2 cua (1^2 + 2^2)  = can5

#repr
print('a')
print(repr('a'))

s= 'a'
a=3
print(f"{s!r}")
print(f"{a!r}")







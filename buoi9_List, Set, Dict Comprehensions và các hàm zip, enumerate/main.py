list =[4,100,5,6]

for value in list:
    print(value)

#tuple
tup = (4,100,5,6)
for value in list:
    print(value)

#set
tup = {4,100,5,6}
for value in list:
    print(value)

#dict
d={
    'a':1,
    'b':2,
    'c':3
}
print(type(d))

for key in d:
    print(key)

for value in d.values():
    print(value)

for item in d.items():
    print(item)

for item in d.items():
    key,value = item
    print(key)
    print(value)
    print('-' * 20)

# iterable là những cái mà mình có thể dùng vòng for duyệt qua nó đc (list,tuple,set,dict...)

#list  comperhensions

# List Comprehension
"""
+ là cú pháp cho phép chúng ta rút gọn một đoạn code dài dòng
+ luôn tạo ra một danh sách (list) mới
+ biến nhận giá trị sau for sẽ không tồn tại khi kết thúc
"""
# Lấy ra một danh sách chứa các loại hoa quả bắt đầu với ký tự 'a'
# một cách thông thường chúng ta sẽ ghi:
fruits = ["apple", "banana", "orange", "kiwi", "mango", "cherry"]

new_list = []

for fruit in fruits:
    if 'a' in fruit: # Kiểm tra ký tự 'a' có nằm trong chuỗi fruit hay không ?
        new_list.append(fruit)       
print(new_list)

# Sử dụng list comprehension
new_list = [fruit for fruit in fruits if 'a' in fruit]
print(new_list)

#####
lst = [1,2,3,4]

#new_lst = [2,4,6,8]
new_lst = []

for x in lst:
    val = x * 2 
    new_lst.append(val)
print(new_lst)

new_lst = [val *2  for val in lst]
print(new_lst)
######


# Sử dụng set comprehension
new_set = {fruit for fruit in fruits if fruit.startswith('a')} # Lấy ra một set các phần tử bắt đầu với 'a'
print(new_set)

###
set_a ={'a','b','c'}
#is
new_set = {s.upper()  for s in set_a}
print(new_set)
###


# Sử dụng Dict comprehension
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# Dict comprehension
# new_d = {
#     i[0]: i[1] * 2
#     for i in d.items()
# }

# Có thể viết sử dụng cú pháp unpacking cũng tương tự
new_d = {
    k: v * 2
    for k, v in d.items()
}

print(new_d)


'''
zip 
enumerate
'''

#zip

# Hàm zip để kết hợp hai hay nhiều iterable (cái có thể for được như: list, tuple, set, dict)
# Nó kết hợp theo cách như sau:
"""
* lấy iterable có len nhỏ nhất làm chuẩn
* lấy giá trị thứ nhất của iterable1 và irterable2, ... kết hợp với nhau => tuple
* zip trả về một zip object chứa một loạt các tuple tương ứng như trên
"""
lst1= ['a','b','c','d']
lst1 = list("abcd") # list - ['a', 'b', 'c', 'd']
lst2 = (1, 2, 3, 4, 5) # tuple

print(list(zip(lst1, lst2))) # List[tuple] vì zip object khi in ra không thể đọc được các giá trị bên trong


#enumerate  trả về một dãy tuple => (),(),()

# Hàm enumerate trả về một enumerate object chứa một loạt các tuple (vị trí, giá trị) của mỗi item trong iterable truyền vào
lst = ['aa', 'bb', 'cc', 'dd']
print(list(enumerate(lst)))



#
lst1 = ('a','b','c')
lst2 = (1,2,3)

print(list(zip(lst1,lst2)))
print(dict(zip(lst1,lst2)))

#1 dict
student = {
    'name': 'Bob',
    'age':23,
    'gender':'male'
}


#vidu
lst = [1,2,3,4]

new_list = []
for x in lst:
    new_list.append(x**3)
#print(x) gan gia tri cho moi lan lap nen se k bi loi
print(new_list)

new_list = [i**3 for i in lst]
#print(v) truy cap ben ngoai se bi loi
print(new_list)

#lay ra nhung so le de cong vao
numbers = [100,34,56,78,88,-46,3,5,7,-11]
new_lst = [v for v in numbers if v % 2 !=0]
print(new_lst)
print(sum(new_lst))

#c1
new_lst = [v*2 if v % 2 ==0 else v *3 for v in numbers]
print(new_lst)
#c2
new_lst=[]
for x in numbers:
    if x%2 ==0:
        new_lst.append(x*2)
    else:
        new_lst.append(x*3)
print(new_lst)


#zip
#enumberate =>  1 loatj cac tuple(),(),()
#      0 1 2 3
lst = [1,2,3,4]
#{i} - {value}
for item in enumerate(lst):
    idx,value = item
    print(f"{idx} - {value}")


for item in enumerate(lst,start=1):
    idx,value = item
    print(f"{idx} - {value}")

for item in enumerate(lst,start=1):
    print(f"{idx} - {value}")


# for item in zip(enumerate(lst,start=1)):
#     print(f"{idx} - {value}") looi k du gias tri minh co the trich xuat khi dang yeu cau la 2 gia trij ma dang chi co 1

#print(list(zip(enumerate(lst,start=1))))


# in ra nhuwng gia tri ow chi so le?
# 4 => range(4) => 0,1,2,3
print(list(range(len(lst))))
for i in range(len(lst)):
    if i % 2 !=0:
        print(i,lst[i])


for i,v in enumerate(lst):
    if i % 2 !=0:
        print(i,v)


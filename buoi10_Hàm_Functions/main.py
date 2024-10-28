# """
# python functions
# """

# # tham so mac dinh
# #
# def my_func():
#     print("Hello wword!")

# my_func()


# #
# def my_func(msg):
#     print(msg)

# my_func("HEloo")


# #
# def show_full_name(fname, lname):
#     print(f"{fname} {lname}")

# show_full_name("Jon","Doe")


# #
# def show_full_name(fname, lname):
#     print(f"{fname} {lname}")


# show_full_name("Jon")


# #
# def show_full_name(fname, lname="Doe"):
#     print(f"{fname} {lname}")


# show_full_name("Jon")



# #return
# def get_full_name(fname, lname="Doe"):
#     return f"{fname} {lname}"
# # return cac ham phia sau se khong chay nua
# #phai tao mot bien de goi ham get_full_name
# full_name = get_full_name("Jon")


# print(full_name)


# #
# def get_full_name(fname, lname="Doe"):
#     if fname:
#         return f"{fname} {lname}"
#     return f"Kenny {lname}"


# full_name = get_full_name("")
# print(full_name)
# # 

# #
# def get_full_name(fname, lname="Doe"):
#     if fname:
#         return f"{fname} {lname}"
#     return f"Kenny {lname}"


# full_name = get_full_name(fname="Joe")
# print(full_name)
# # 

# #
# def get_full_name(fname, lname="Doe"):
#     if fname:
#         return f"{fname} {lname}"
#     return f"Kenny {lname}"


# full_name = get_full_name(lname="Jenlyy",fname="Joe")
# print(full_name)

# #
# full_name = get_full_name(lname="Jenlyy",fname="Joe")
# print(full_name)


# def get_full_name(fname, lname="Doe"):
#     if fname:
#         return f"{fname} {lname}"
#     return f"Kenny {lname}"


# #cong 2 so
# #
# def add(x,y):
#     return x+y

# print(add(10,20))

# #
# def add(x,y=10):
#     return x+y


# print(add(x=10))


# #
# def add(x,y=40):
#     return x+y


# print(add(y=10))

# #
# def add(x,y=40):
#     return x+y


# print(add(y=10,x=100))


# #
# def func(lst=[]):
#     lst.append(2)
#     print(lst)


# func()
# func()

# #friends
# friends = ["kenny","Bob","Jen"]

# def my_func():
#     #friends = friends + ["Joe"]
#     f = friends + ["Joe"]
#     #thay friends = f de khong bi loi
#     print(f)


# my_func()


# #bien cuc bo la nam trong ham``
# # bien toan cuc. nam ben ngoai ham``
# # khong tao bien khi tham chieu toi' no'

# #lambda ham` khong ten

# add= lambda x,y: x +y
# print(add(1,2))


# #firstclass functions
# là 1 hàm mà nó lại  nhận vào 1 hàm khác 
# hàm có thể coi là cái biến mình có thể gán cho 1 cái biến 1 giá trị khác

def greet(msg):
    print("Hello" + msg)
    return None
# tat cả hàm trong python đều trả về giá trị mặc định là None

# GÁN TÊN HÀM CHO 1 BIẾN KHÁC
hello = greet

print(hello("jen"))



# 1 hàm trong python không thể để là trống được 
# vậy nên ta có pass để trong hàm python, muốn tạo hàm trống ta xử dụng pass
def func():
    pass 

# toán tử *agrs
#  * định nghĩa trong hàm

def add(x,y,z,t):
    return x+ y+ z+ t 
print(add(1, 2, 3, 4, 5))

# tap hop ca doi so vao trong  1 tuple agrs 
# 1 dau * la doi so vitri // 2 dau ** la doi so' co ten
def add(*agrs):
    print(type(agrs))
    return sum(agrs)
print(add(1, 2, 3, 4, 5))

# * cho loi` goi. ham`
lst = [4, 3, 2, 1]
print(*lst)


# 
lst = [3 ,10, 6 ,5 , 7]
#  lay gia trị đầu tiên, giũa , cuối
first, *mid, last = lst

print (first)
print(mid)
print(last)

# nâng cao về hàm
def add(*lst, operation):
    return operation(lst)

print(add(1, 2, 3, 4, operation=sum))

# về hàm trể về None
#  mac đinh tat ca ham trong python duoc trả về None
def my_func():
    print(" hello")

my_func()
print(my_func())

lst = []

a = lst.append(23)
# lst.append(23) chỉ thực hiện ghành dộng chứ không trả về giá trị cụ thể nên trường hợp này trả về None 
print(a)

lst = [[]] * 5
print(lst)


lst = [[]] * 5
lst[1].append(2)
print(lst)
#  khong nen nhan 1 so với 1 list
# ban dau tao ra lst [] sau đó tạo ra 5 tham chieu và trỏ tới [] tat cả sẽ bị ảnh hưởng


lst = [[] for _ in range(5)]
lst[1].append(2)
print(lst)
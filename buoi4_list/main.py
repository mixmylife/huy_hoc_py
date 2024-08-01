# """
# + list lồng list (list in list)
# + copy list
# +list slicing => new list
# """
#list in list
friends = [["bob",23],["Duyen",22],["Huy",22]]
#print(type(friends[0]))
print(friends[0][0])
print(friends[1][1])
#print(friends[100][1])

#copy list
lst1 = [1,3,2]
lst2 =lst1
lst2 = lst1.copy()
#is 
#id trả về 1 cái id duy nhất của mỗi giá trị mình đang truyền vào id(địa chỉ,giá trị)
print(id(lst1),id(lst2))
print(lst1 is lst2)
print(lst1 == lst2)


#list slicing 
# a[Start:stop:step]
# Cú pháp: list[start:stop:step]
# start - vị trí bắt đầu lấy giá trị từ danh sách gốc
# stop - vị trí kết thúc (không lấy giá trị tại đó)
# step: bước nhảy - nghĩa là: tăng lên vị trí thứ mấy so với vị trí start
# Nếu không chỉ ra giá trị start thì start mặc định là 0 (start = 0)
# Nếu không chỉ ra giá trị stop thì stop mặc định là len(list gốc) (stop = len(list gốc))
# Nếu không chỉ ra giá trị step thì step mặc định là 1 (step = 1)
# Nhớ: list slicing luôn tạo ra một danh sách mới hoàn toàn, không phải danh sách ban đầu (gốc)

a = [1,3,10,200,45]
new_list = a[0:2:1]
print(new_list)

new_list = a[0:5:2]
print(new_list)

# từ 1 đến hết
new_list = a[1:]
print(new_list)

new_list = a[1:4]
print(new_list)

#lấy ở giữa bỏ 2 đầu mút
new_list = a[1:-1]
print(new_list)

new_list = a[:]
print(new_list)

#lật ngược list a 
new_list = a[::-1]
print(new_list)

print(a[::-1] is a)


#khác nhau như nào
b =257 #(python tạo ra int(257) sau đó mới gán cho b để tham chiếu)
# [5,266]  
 


# revert là trên danh sách ban đầu 
# list slicing thì ra 1 list hoàn toàn mới

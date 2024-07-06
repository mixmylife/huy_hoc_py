

numbers = [1,2,3.5,4,1]
print(type(numbers))
print(numbers)
print(numbers[2])
print(numbers[-1])
print(numbers[-3])

#xoa trong list
numbers.remove(-1)
print(numbers)
numbers.remove(-1000)
print(numbers)

#lay ra gia tri cuoi cung va xoa gia tri do di
last_value = numbers.pop()
print(last_value)
print(numbers)

#them mot so vao cuoi danh sach va in ra 
numbers.append(100)
print(numbers)
 
 #muon them vao cuoi khong phai la 1 gia tri ma 1 lisst khac
numbers.extend([9,1000,22,5])

# khong muon gia tri dau tien la 1 ma la 1 gia tri khac
numbers[0] = 19

# dem so luong  cua gia tri "1" trong list
amount = numbers.count(1) 
amount = numbers.count(1000) 
print(amount)

#xoa tat ca gia tri trong list
numbers.clear()
print(numbers)

#muon tim tong so luong gia trij ben trong hay la chieu dai cua mot list
amountt = len(numbers)
print(amountt)

#dir(list) - cac phuong thuc lie nqua  den list

#insert 
numbers.insert(0,1000)
numbers.insert(1000,1000) # chen motj soo duwong khong cos trong list thif sex in ve sau list nguowcj laji so am thi in len dau
numbers.insert(-10,1000)
print(numbers)

#index tra ve chi so cua 1 gia tri ma minh truyen vao ham index
index_of_3p5 = numbers.index(3.5)
print(index_of_3p5) # tra ve vij tri 2 cos gia trij laf 3.5
index_of_3p5 = numbers.index(-10000) # loi vi trong list khong nam trong list


#reverse    se dao nguoc 1 danh sach
numbers.reverse()
print(numbers)

#sort sap xep danh sach theo thu tu tang hay giam
numbers.sort(reverse=True) #desc
numbers.sort() #asc
print(numbers)

friends = ["Kenny", "Jack", "John", "Jose", "Mary"]
print("Ban đầu:", friends)

friends.remove("john".title())
print(friends)
# cung la xoa 1 gia tri minh chon trong list
del friends[-1]
print(friends)

numbers = [12,34,36,-100,67]
max_value = max(numbers)
print(max_value)

min_vl = min(numbers)
print(min_vl)
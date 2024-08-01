'''
+ Advanced Set
+ dictionary key:value
+sum,len,min,mã,join

'''
#Advanced Set

set1 = {1,4,3,2}
set2={2,3,10,-10}
set4={10,11,20}

set3 = set1.intersection(set2) 
# bat buoc phí trước intersection phải là set 
# thì mới gọi đc intersection va cái truyền vào 
# intersection có thể là set, tuple,list
print(set3)

print(set1 & set2)
#với & thì bắt buộc phải giống
# nhau bắt  buộc phải là set

set3 = set1.difference(set2)
print(set3)
# bat buoc phí trước difference phải là set 
# thì mới gọi đc difference va cái truyền vào 
# difference có thể là set, tuple,list

print(set1 - set2)
#với - thì bắt buộc phải giống
# nhau bắt  buộc phải là set


set3 = set2.difference(set1)
print(set3)

print(set2 - set1)


#lấy tất cả 

set3 = set1.union(set2).union(set4)
print(set3)

print(set1 | set2 | set4) #pire

#lấy tất cả nhưn trừ phần chung của tất cả 
set3 = set1.symmetric_difference(set2)
print(set3)

print(set1 ^ set2)


#dictionary key:value

import json

student = {
    "Name" : "Bob",
    "age":22,
    "grades":{45,64,34,54,64}
}

# print(json.dumps(student,indent=4))

# value = student["Name"]
# print(value)


value = student.get("id","SV001")
print(value)
#hoặc
student["id"] = "SV001"
print(student)

student["Name"] = "Duyn"
print(student)

#update

student.update(id = "SV001", gender = "Female")
print(json.dumps(student,indent=4))
#hoặc
info = {
    'id':"SV001",
    'gender':'male'
}
student.update(info)
print(json.dumps(student,indent=4))


info = [
    ('id',"SV001"),
    ('gender','male')
]
student.update(info)
print(json.dumps(student,indent=4))


#xóa
student.pop('name')
print(json.dumps(student,indent=4))

value =student.pop('name')
print(value)
print(json.dumps(student,indent=4))
#hoặc
del student["name"] # XÓA KHỎI BỘ NHỚ THU HỒI VỀ HỆ ĐIỀU HÀNH
print(json.dumps(student,indent=4))

#lấy tra phần tử cuối cùng và xóa trong dictionary
tup = student.popitem()
print(tup)
print(json.dumps(student,indent=4))

#keys
keys = list(student) # in ra theo dạng list
print(keys)

values = list(student.values())
print(values)

items = list(student.items)
print(items)


#clear 
student.clear()
print(student)


#hàm 
#sum

lst = [[1,2,3,4]]


total = sum(lst)
print(total)

lst2 = []
total1 = sum(lst2)
print(total)

total = sum(lst,10)
print(total)

total = sum(lst,10)
print(total)

total = sum(lst,[0])
print(total)


lst1 = [[1,2,3,4],[10,6,9,42]]
total = sum(lst,[0])
print(total)

#len
lst = ['a','b','c','d','f']
print(len(lst))

lst = []
print(len(lst))

#min
lst = ['a','b','c','d','f']
print(min(lst)) #loi min khong đươc trống

#max
lst = ['a','b','c','d','f']
print(min(lst)) #loi max khong đươc trống

#join 

lst = [4,3,2,1]
s = '-'.join(map(str(lst)))
print(s) 
# sẽ bọ lỗi bởi vì list trên đang chưa số không
# phải chuỗi nên mình cần convert list về chuỗi thì mới chạy đc 
# convert như trên map(str(lst))

lst = ['4','3','2','1']
s = '-'.join(lst)
print(s) 

lst = ['4','3','2',1]
s = '-'.join(map(str(lst)))
print(s) 

lst = ['a','b','c']
print(sum(lst)) # lỗi sum chỉ sử dụng trên số

lst = ['4','2','4']
print(sum(lst)) # lỗi sum chỉ sử dụng trên số đây vẫn kiểu str


#hàm map 
# truyền vào 1 funcition để convert  
# từng giá trị về 1 cái dang nào đó mà funcition thực hiện
def double(x) :
    return x *2

print(list(map(double,[1,2,4,3])))

print(set(map(double,[1,2,4,3])))

#print(dict(map(double,[1,2,4,3])))#lỗi
#OOP - Là lập trình hướng đối tượng (có class, object để quản lý và dễ đọc)



class Student:
    # def __init__(self, name, age) :
    #     self.name = name
    #     self.age  = age

    def __init__(self, name, age, address) :
        self.name = name
        self.age  = age
        self.address = address
    
    def show_info(self):
        print(f''' Student info 
Name: {self.name}
Age:  {self.age}
Address: {self.address}''')

    #dunder method
    def __str__(self):
        return"<Student(name={self.name}, age={self.age})>"

    def __gt__(self, other):
        return self.age > other.age
    


# _name_
# student_one = Student("Bob",23)
# student_tow = Student("Mary",33)


# print(student_one.name)
# print(student_one.age)
# print(student_one)

#print(student_one > student_tow)

student_one = Student("Bob",22, "New York")

student_one.show_info() 
Student.show_info(student_one)




class People:
    def __init__(self, birth_year):
        self.birth_year = birth_year


#Khi goị get_age dòng 58 không có dấu ngoặc tròn đằng sau mà vẫn ra được kết quả thì dùng @property

    #@property # để xác định và coi nó như là 1 thuộc tính 1 đặc diểm của People không phải hàm nên ta bỏ được ()
    def get_age(self):
        return 2024 - self.brith_year

people1 = People(1992)
age = people1.get_age()
#age = people1.get_age
print(age)




class Human:
    def __init__(self, name):
        self.name = name

    # def __str__(self):
    #     return f"{self.name}"

#Kế thừa
class Studentt(Human):
    def __init__(self, name, age):# thuộc tính name và age
        super().__init__(name)
        self.age = age

    def __str__(self):
        return f"Name : {self.name}, age: {self.age}"

student_1 = Studentt("Joe",22)
print(student_1)

#__init__ dùng để, được gọi khi mình gọi đến class thì hàm init sẽ đc gọi 
# people1 = People(1992) init đc gọi 


class Stude:
    #contructor function hàm khởi tạo mặc định
    def __init__(self, name="Bob"):
        self.name = name
    
    def __repr__(self):
        return f"<Stdent(name = {self.name})>"

    def __str__(self):
        return f"name : {self.name})>"


#ưu tiên gọi str trước 

s1 = Stude()
s2 = Stude("Joe")
print(s1.name)
print(s2.name)
print(repr(s2))
print(s2.__str__())
print(str(s2))


x = 5 #int (5)
print(type(x))
# gọi dunder int
print(True + 1 )
print(True + 1.5)

#gọi dunder mutiply
print('*' * 5)

class Hello:
    def show(self):
        print("Hello")

hl1= Hello()
hl1.show()


#Đếm số đối tượng tạo ra 
class user :#= class user(object)
    count = 0

    def __init__(self):
        user.count +=1    

user1 =user()
print(user.count)
user2 =user()
print(user.count)



print(__name__)


#'''About'''
print(__doc__)





#File (Đọc ghi file)
"""
b1: open
b2: process
b3: close
"""
#
fb = open("data.txt", mode="r") # reading

data = fb.read()
print(data)

fb.close()

#
fp= open("test.txt", mode = "w") #writing sẽ xóa dữ liệu cũ thêm dữ liệu mới

fp.write("Kenny Huy")

fp.close()

#
fp= open("testt.txt", mode = "a") #appen sẽ thêm dữ liệu  mới vào sau dữ liệu cũ

fp.write("\nKenny Huy") # new line 

fp.close()

#
lst = ["a", 1, True, "c", 4.5]

fb = open("data.txt", mode="w")

fb.write(' - '.join(map(str, lst)))

fb.close()









        
         
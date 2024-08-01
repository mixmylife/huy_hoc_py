# 1. Cho danh sách (list) friends = ["Jen", "Jack", "Kenny", "Jelly", "Bob", "Henry", "Anne"]
# Yêu cầu:

friends = ["Jen", "Jack", "Kenny", "Jelly", "Bob", "Henry", "Anne"]
print(friends)
# a. Lấy ra 4 người bạn đầu tiên trong friends
friends_new = friends[0:4:1]
print("Danh sách 4 người đầu tiên là: ", friends_new)

# b. Lấy ra 4 người bạn cuối trong friends
friends_new = friends[-1:-5:1]
friends_new = friends_new[::-1]
print("Danh sách 4 ngời cuối cùng là:", friends_new)
# Khi bạn sử dụng cú pháp slicing friends[-1:-5:1], nó sẽ không hoạt động như mong đợi 
# vì bước (step) 1 đi từ trái sang phải trong danh sách,
# nhưng -1 bắt đầu từ phải sang trái. Để lấy ra 4 người bạn cuối cùng, 
# bạn cần sử dụng bước -1 và sau đó đảo ngược kết quả.

friends_new = friends[-4:]
print("Danh sách 4 người bạn cuối cùng là:", friends_new)


# c. Đảo ngược danh sách friends
friends_new = friends[::-1]
print("Danh sáchsau khi được đảo ngược :", friends_new)

# d. Lấy ra những người bạn từ vị trí 1 đến hết
friends_new = friends[1:]
print("Danh sách những người bạn từ vị trí 1 đến hết :", friends_new)

# e. Copy danh sách ban đầu thành một danh sách mới
friends_news = friends.copy()
print("Danh sách của friends_new :",friends_news)

# f. Lấy ra những người bạn từ vị trí 2 đến sát cuối
print("Danh sách ban đầu của list phờ ren:",friends)
friends_new = friends[2:-1:1]
print("Danh sách những người bạn từ vị trí 2 đến sát cuối:", friends_new)

# 2.Cho danh sách các sinh viên chứa thông tin của mỗi sinh viên [id, tên, tuổi] như sau:
# students = [["SV001", "Bob", 23], ["SV002", "Kenny", 34], ["SV003", "Henry", 45]]
# Yêu cầu:

students = [["SV001", "Bob", 23], ["SV002", "Kenny", 34], ["SV003", "Henry", 45]]
# a. Lấy ra thông tin của sinh viên thứ nhất và in ra định dạng "ID: {id}, name: {name} - age: {age}"
students_one= students[0]
students_id = students_one[0]
students_name = students_one[1]
students_age= students_one[2]
print(f"Thông tin sinh vien gồm Id: {students_id}, name:{students_name}, age:{students_age}")
#hoặc
print("Thông tin sinh viên gồm Id: {}, name: {}, age: {}".format(students_id, students_name, students_age))
# dấu ngowacj nhọn để lấy type của nó 

# b. Lấy ra tuổi của sinh viên thứ hai
student_two = students[1]
student_age = student_two[2]
print("Thông tin tuổi của sinh viên thứ 2 'Kenny' là: ",students_age)

# c. Lấy ra thông tin hai sinh viên cuối cùng
students_new = students[-2::]
print("Thông tin của 2 sinh viên cuối cùng là:",students_new)

# d. Lấy ra id của sinh viên thứ ba
# student_three = students[2]
# student_id = student_three[3]
# print(f"Thông tin id của sinh viên thứ 3 'Henry' là:,{students_id} ")
student3_id = students[-1][0]
print("Id của sinh viên thứ 3 là:",student3_id)
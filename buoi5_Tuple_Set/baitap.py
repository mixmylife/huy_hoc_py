'''1.Cho một list chứa các tuple như sau: friends = [("Bob", "Male"), ("Anna", "Female"), ("Max", "Male")]
a. Cho biết chiều dài của friends
b. Lấy ra phần tử đầu, cuối và giữa và kiểm tra kiểu của chúng
c. Nhập vào tên (name) và giới tính (gender) của một người bạn sau đó append vào friends tuple gồm hai giá trị (name, gender)'''

friends = [("Bob", "Male"), ("Anna", "Female"), ("Max", "Male")]

#a
friends_new = len(friends)
print("Có tất cả số phần tử trong friends",friends_new)

#b
phan_tu_dau =type(friends[0])
print("Kiểu dữ liệu của phần tử đầu",phan_tu_dau)

phan_tu_cuoi =type(friends[-1])
print("Kiểu dữ liệu của phần tử cuối",phan_tu_cuoi)

giua = len(friends)//2
phần_tử_giữa =type(friends[giua])
# gop_vao = abs(len(friends)//2)
print("Kiểu dữ liệu của phần tử giữa",phần_tử_giữa)

#c
fren_new = str(input("Nhập tên vào đây:"))
fren_news = str(input("Nhập giới tính vào đây:"))

friends.append([(fren_new),(fren_news)])
print(friends)

fren_new = str(input("Nhập tên vào đây:"))
fren_news = str(input("Nhập giới tính vào đây:"))
friends.insert(0,[(fren_new),(fren_news)])
print(friends)

'''
2. Tạo một set trống có tên là set_a
a. Thêm 'Anna' vào set_a
b. Thêm một tuple ('Kenny', 'Jen', 'Danny')
c. In ra set_a và tính chiều dài của nó
d. Xóa 'Jen' ra khỏi set_a
e. Xóa tất cả các giá trị từ set_a'''


# add(element) thêm một phần tử đơn lẻ vào set.
# update(iterable) thêm các phần tử từ một iterable (như list, tuple, set) vào set.


set_a = set()

#a 
set_a.add('Anna')
print(set_a)

#b
set_a = set()
tup =('Kenny','Jen','Danny')
set_a.update(tup)
print(set_a)

#c
print(set_a)
print("Có tất cả số phần tử là ", len(set_a))

# d. Xóa 'Jen' ra khỏi set_a
set_a.remove('Jen')



#e
set_a.clear()
print(set_a)



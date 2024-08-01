# Nhập vào một danh sách những số nguyên và hiển thị gấp đôi của các số trong danh sách sử dụng list comprehens


list_1 = [int(n) for n in input("nhap vao danh sach so nguyen:\n").split()]
new_list = [i *2 for i in list_1]
print(new_list)


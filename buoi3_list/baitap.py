import io
import sys

# 1.Tạo một movies list chứa tên các bộ phim đã xem
Movies =["captain america","Mình yêu nhau bìn yên thôi","Em và Anh","Tất cả vì nhau","Python"]
print (Movies)

# 2.Sử dụng hàm input để nhập vào một bộ phim khác không có trong movies list
movie_new = str(input("Nhập bộ phim mới tại đây :"))

# 3.Thêm bộ phim vừa nhập vào cuối của danh sách movies
Movies.append(movie_new)
print("List phim sau khi được thêm :", Movies)

# 4.In ra bộ phim đầu tiên, cuối cùng và ở giữa movies list
print(Movies[0])
print(Movies[-1])

amount = len(movie_new)
print(Movies[amount//2])

# 5.Tính tổng bộ phim có trong movies
amount = len(movie_new)
print("Tổng số bộ phim trong danh sách là : ",amount)

# 6.Xóa bộ phim đầu và cuối trong movies
del Movies[0] #Movies.remove(Movies[0])
print(Movies)

del Movies[-1] #Movies.remove(Movies[0])
print(Movies)
# 7.Lấy ra và xóa bộ phim cuối cùng trong movies
last_movie = Movies.pop()
print(Movies)

first_movie = Movies.pop(0)
print(Movies)

# 8.Chèn một bộ phim bất kỳ vào đầu danh sách movies
Them_Phim = input("Phim mới cần thêm vào :")
Movies.insert(0,Them_Phim)
print(Movies)

#Thêm đây để xuống dưới vidu 9, 10 dùng sau
Movies.extend(["One Piece", "gió","Nhàn","Tiền","One Piece"])
print(Movies)

# 9.Đếm số bộ phim có tiêu đề là "One Piece"
Dem_Phim_OP = Movies.count("One Piece")
print(Movies)
print(Dem_Phim_OP)

# 10.Tìm vị trí của bộ phim có tên là "gió"
Tim_Kiem_Vi_Tri = Movies.index("gió")
print(Movies)
print(Tim_Kiem_Vi_Tri)

# 11.Thêm một danh sách bộ phim khác vào cuối danh sách movies ban đầu
Movies.extend(["One Piece", "gió","Nhàn","Tiền","One Piece"])

# 12.Xóa tất cả các bộ phim có trong danh sách
Movies.clear()
print(Movies)
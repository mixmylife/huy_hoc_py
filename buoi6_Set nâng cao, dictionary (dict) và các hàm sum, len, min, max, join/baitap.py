# # 1. Cho hai tập hợp (set)

# art_students = {"John", "Max", "Anna", "Bob", "Obito"}

# math_students = {"Max", "Mery", "David", "Anna", "Naruto", "John"}

# # Tìm những người bạn học cả vẽ lẫn toán
# set_art_math = art_students.intersection(math_students)
# #or
# print(art_students & math_students)

# print(set_art_math)

# # Tìm những người bạn học vẽ nhưng không học toán
# set_art = art_students.difference(math_students)
# #or 
# print(art_students - math_students)

# print(set_art)

# # Tìm những người bạn học toán nhưng không học vẽ
# set_math = math_students.difference(art_students)
# #or 
# print(math_students - art_students)

# print(set_math)

# # Tìm những người bạn học vẽ hay toán không phải cả hai
# set_khong_chung = (art_students.symmetric_difference(math_students))
# # or
# print(art_students ^ math_students)

# print(set_khong_chung)



# # Tìm tất cả những người bạn
# all_students = art_students.union(math_students)
#  #or
# print(art_students | math_students)

# print(all_students)



# 2.Cho dict sau:

import json

album_info = {
    "album_name": "The Dark Side of the Moon",
    "band": "Pink Floyd",
    "release_year": 1973,
    "track_list": [
        "Speak to Me",
        "Breathe",
        "On the Run",
        "Time",
        "The Great Gig in the Sky",
        "Money",
        "Us and Them",
        "Any Colour You Like",
        "Brain Damage",
        "Eclipse"
    ]
}


# Yêu cầu:

# 1.Lấy ra giá trị của các key sau: album_name, release_year bằng hai cách
valuename = album_info.get("album_name")
print(valuename)
valuename = album_info.get("release_year")
print(valuename)


album_info["album_name"]
print(album_info)
album_info["release_year"]
print(album_info)

# 2.Thay đổi giá trị của key: release_year từ 1973 thành 1971
album_info.update(release_year = 1971)
print(json.dumps(album_info,indent=4))

# 3.Xóa phần tử với key là track_list
# value =album_info.pop('track_list')
# print(value)
# print(json.dumps(album_info,indent=4))

del album_info["track_list"] # XÓA KHỎI BỘ NHỚ THU HỒI VỀ HỆ ĐIỀU HÀNH
print(json.dumps(album_info,indent=4))

# 4.Thêm một key mới là amount = 2000 bằng hai cách
album_info["amount"] =2000
album_info.update(amount = 2000)
print(json.dumps(album_info,indent=4))


# 5.Làm trống dict: album_info
album_info.clear()
print(album_info)
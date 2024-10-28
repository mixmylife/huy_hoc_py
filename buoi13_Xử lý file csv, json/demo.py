# Xử lý file CSV

# with open ("D:/Python/hoc_python/buoi13_Xử lý file csv, json/topSubscribed.csv", mode = "r", encoding="utf8") as sub:
#     # country.readline() khoong nen dungf nhieu du lieu doc rat lau
#     for line in sub :
#         print(line.strip())

# import csv 
# import json
# with open ("D:/Python/hoc_python/buoi13_Xử lý file csv, json/topSubscribed.csv", mode = "r", encoding="utf8") as sub:
#     csv_file = csv.DictReader(sub)
#     #  print(list(csv_file)) # convert vee list[dict]
#     lst = list(csv_file)
#     print(json.dumps(lst, indent=4))

# import csv 
# import json
# with open ("D:/Python/hoc_python/buoi13_Xử lý file csv, json/topSubscribed.csv", mode = "r", encoding="utf8") as sub:
#     csv_file = csv.DictReader(sub)
#     #  print(list(csv_file)) # convert vee list[dict]
#     lst = list(csv_file)
#     for item in lst:
#         print(item)




# Xử lý file Json

# import json 
# # đọc dữ lieu json
# with open("D:/Python/hoc_python/buoi13_Xử lý file csv, json/test.json", mode="r") as file:
#     lst = json.load(file) # de doc du lieu vao file json  con ham dumps la ghi du lieu vao file json
#     print(json.dumps(lst, indent=4))

# #ghi dữ liệu vào json
# student =[{
#     'name':"Bob",
#     'age': 23
#     },
#     {
#     'name':"Joe",
#     'age': 22
#     }
# ]

# with open("D:/Python/hoc_python/buoi13_Xử lý file csv, json/data1.json", mode="w") as file:
#     json.dump(student, file, indent=4)
    




# # Xử lý với CSV tiếp
# import csv 

# header = ["id", "name", "age"]
# student = ["SV001","Bob",24]

# with open("test1.csv", mode="w", newline='') as file:
#     csv_writer = csv.writer(file)
#     csv_writer.writerow(header)
#     csv_writer.writerow(student)

 
# mode ="r+" vừa đọc vừa ghi

# Hamf trong json
# dupm- ghi du lieu vao file json
# dupms - chuyển doi 1 list[dict] hay dict thanh 1 chuoi
# load - doc du lieu tu file json -> list[dict] hay dict
# loads - chuyen doi 1 string co danng dict hay list[dict] thanh list[dict] hay dict tương ứng

import json
data = '{"name": "Bob", "age":23}'
_dict = json.loads(data)
print(_dict)


# Hàm trong CSV
# DictReader - tạo ra list[dict]
# writer()
# writerow
# writerows

# mode ="x" khi file đó chưa tồn tại nó sẽ đc tạo ra list trống



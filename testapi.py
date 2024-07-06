import json

# Đọc dữ liệu từ file JSON
with open('D:\DUANINDA\aokhoacnam.json', 'r') as file:
    data = json.load(file)

# Xử lý dữ liệu
# Ví dụ: In ra tất cả các key và giá trị trong JSON
for key, value in data.items():
    print(f'{key}: {value}')



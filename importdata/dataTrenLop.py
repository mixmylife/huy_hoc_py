import json
import pandas as pd
# Đọc dữ liệu từ file JSON
with open('https://localhost:7206/api/SinhViens', 'r', encoding='utf-8') as file:
    data = json.load(file)
# Chuyển đổi dữ liệu JSON thành DataFrame của pandas
df = pd.json_normalize(data, 'data') 
# In ra tên các cột trong DataFrame để xác định tên cột chính xác
print("Các cột trong DataFrame:")
print(df.columns)
# Sử dụng tên cột từ DataFrame để chọn các cột cần thiết
selected_columns = ['id', 'maSV', "hoTen", 'ngaySinh', 'maLop'
                     ]
df = df[selected_columns]
# Xuất DataFrame ra file Excel
df.to_excel('D:\\python\\fileImport\\datasv.xlsx', index=False)
# In ra một số dòng đầu tiên của DataFrame
print("Dữ liệu một số dòng đầu tiên của DataFrame:")
print(df.head())
# In ra kích thước của DataFrame
print("\nKích thước của DataFrame:")
print(df.shape)


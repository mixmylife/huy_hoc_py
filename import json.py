import json
import pandas as pd
# Đọc dữ liệu từ file JSON
with open('D:\\DUANINDA\\datatiki_owenshop2.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
# Chuyển đổi dữ liệu JSON thành DataFrame của pandas
df = pd.json_normalize(data, 'data') 
# In ra tên các cột trong DataFrame để xác định tên cột chính xác
print("Các cột trong DataFrame:")
print(df.columns)
# Sử dụng tên cột từ DataFrame để chọn các cột cần thiết
selected_columns = ['id', 'sku', 'name', 'price', 'discount', 'discount_rate', 'seller_product_id', 'original_price',
                    'seller_id', 'seller_name', 'order_route', 'brand_id', 'brand_name', 'primary_category_name', 'productset_id']
df = df[selected_columns]
# Xuất DataFrame ra file Excel
df.to_excel('D:\\DUANINDA\\datatiki.xlsx', index=False)
# In ra một số dòng đầu tiên của DataFrame
print("Dữ liệu một số dòng đầu tiên của DataFrame:")
print(df.head())
# In ra kích thước của DataFrame
print("\nKích thước của DataFrame:")
print(df.shape)


import requests
from bs4 import BeautifulSoup
import pandas as pd

# Lấy nội dung HTML từ trang web
url = 'https://sinhvien.uneti.edu.vn/ket-qua-hoc-tap.html'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Tìm bảng trên trang web
table = soup.find('table')

# Trích xuất dữ liệu từ bảng
data = []
for row in table.find_all('tr'):
    row_data = []
    for cell in row.find_all(['td', 'th']):
        row_data.append(cell.get_text(strip=True))
    data.append(row_data)

# Tạo DataFrame từ dữ liệu
df = pd.DataFrame(data[1:], columns=data[0])

# Lưu DataFrame vào file Excel
df.to_excel('ket_qua_hoc_tap.xlsx', index=False)

print("Đã lưu dữ liệu vào file ket_qua_hoc_tap.xlsx")




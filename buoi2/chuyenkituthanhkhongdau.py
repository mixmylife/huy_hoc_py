from unidecode import unidecode

def remove_accents(input_str):
    # Sử dụng hàm unidecode để chuyển đổi chuỗi Unicode sang chuỗi không dấu
    return unidecode(input_str)

# Chuỗi Unicode đầu vào
unicode_str = "1.Lấy danh sách các khách hàng đã vay số tiền lớn hơn 50 triệu đồng tại các chi nhánh ở thành phố Hà Nội và tên ngân hàng tương ứng 2.Lấy tổng số tiền vay của mỗi khách hàng và sắp xếp giảm dần theo tổng số tiền vay 3.Lấy số tiền vay trung bình tại mỗi chi nhánh 4.Lấy danh sách các khách hàng không có tài khoản gửi 5.Lấy tổng số tiền gửi và số tiền vay của mỗi khách hàng"


# Chuyển đổi chuỗi Unicode sang chuỗi không dấu
result_str = remove_accents(unicode_str)

# In ra kết quả
print("Chuỗi không dấu: ", result_str)

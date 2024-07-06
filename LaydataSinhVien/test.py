# Tính tổng điểm trọng lượng của từng môn
mon_1 = 4 * 1.5
mon_2 = 2 * 2.0
mon_3 = 2 * 3.5
mon_4 = 3 * 1.5
mon_5 = 1 * 3.0
mon_6 = 2 * 2.5
mon_7 = 2 * 3.0
mon_8 = 4 * 3.0
mon_9 = 3 * 2.5
mon_10 = 4 * 3.0
mon_11 = 4 * 3.0
mon_12 = 3 * 2.5
mon_13 = 2 * 3.5
mon_14 = 3 * 3.0
mon_15 = 2 * 3.5

# Tính tổng số tín chỉ đã hoàn thành
tong_tin_chi = 4 + 2 + 2 + 3 + 1 + 2 + 2 + 4 + 3 + 4 + 4 + 3 + 2 + 3 + 2

# Tính tổng trọng lượng điểm
tong_diem_trong_luong = mon_1 + mon_2 + mon_3 + mon_4 + mon_5 + mon_6 + mon_7 + mon_8 + mon_9 + mon_10 + mon_11 + mon_12 + mon_13 + mon_14 + mon_15

# Tính GPA
GPA = tong_diem_trong_luong / tong_tin_chi

print("Tổng trung bình tích lũy trên hệ 4 là:", GPA)

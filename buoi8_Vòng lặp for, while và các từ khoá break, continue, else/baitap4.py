
#Đếm số lượng số nguyên tố trong [1, 100]
dem_nguyenn_to = 0

for n in range(2, 100):
    trang_thai = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            trang_thai = False
            break
    if trang_thai:
        dem_nguyenn_to += 1 

print("So luong so nguyên tố có trong chuỗi là:", dem_nguyenn_to)



count = 0

for n in range(2, 101):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            break
    else:
        count += 1
        
print(count)
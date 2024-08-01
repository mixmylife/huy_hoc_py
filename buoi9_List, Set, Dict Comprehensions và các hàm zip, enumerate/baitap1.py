# Đếm số chẵn và lẻ trong đoạn [0, 1000] theo 2 cách: thông thường và list comprehension

#thông thường

so_chan =0
so_le=0
for i in range(0,1000,1):
    if i % 2 ==0:
        so_chan +=1     
    else:
        so_le +=1
print("Tổng các số chẵn có trong chuối là:",so_chan)
print("Tổng các số chẵn có trong chuối là:",so_le)

# Cách 2: Sử dụng list comprehension
even = sum([1 for n in range(0, 1001) if n % 2 == 0])
odd  = sum([1 for n in range(0, 1001) if n % 2 != 0])

print(f"Số lượng giá trị chẵn trong [0, 1000]\t: {even}")
print(f"Số lượng giá trị lẻ trong [0, 1000]\t: {odd}")

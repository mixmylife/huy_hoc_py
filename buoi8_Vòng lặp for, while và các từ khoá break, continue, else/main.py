for _ in range(5): 
    print("Hello world")


for i in range(1,21):
    if i % 2==0:
        print(i,end='')


#WHILE
s = input('>')
while s !='q':
    print("hello")
    s = input('>')

#for lồng for 
for i in range(5):
    for j in range(3):
        print(i,j, sep="-")


#break thoat hoàn toàn ra khỏi vòng lặp chứa nó
for i in range(1,21):
    if i >5:
        break
    print(i,end=' ')


#continue bỏ qua lần lặp hiện tại, câu lệnh dưới nó và chuyển lần lặp mới
for i in range(1,21):
    if i % 2 == 0:
        continue
    print(i,end=' ')

#else 
for i in range(1,21):
    print(i,end=' ')
else:
    print("Success")


#Từ khóa else với vòng lặp for   
# In ra các số nguyên tố trong đoạn [2, 100]
for n in range(2, 101):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            break
    else:
        print(n, end=' ')

print(list(range(10)))

print(range(True))


"""
Hàm range chỉ nhận các giá trị số nguyên (int) của start, stop, step không phải số thực (float)
nên truyền vào số thực cho range sẽ bị lỗi
"""
print(range(10.5))
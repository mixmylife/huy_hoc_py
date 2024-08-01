'''
if - elif - else
'''

if 1 > 0 :
    print("1>0")
else:
    print("1<0")


n = int(input("n ="))

if n >0:
    print("So duong")
elif n< 0:
    print("So aam")
else:
    print("So 0")


# #chu y':
# Về cú pháp:
# Cuối if, elif, else phải có dấu hai chấm (:) biểu thị khối lệnh
# Những dòng print trong đoạn code trên bị thụt lề (thường là một Tab = 4 spaces) gọi là Indentation
# Thụt lề rất quan trọng trong các câu lệnh if, for, while, def nên mọi người phải chú ý
# So sánh bằng sau câu lệnh if thì sử dụng toán tử == (bằng bằng) không phải một dấu = (phép gán - định nghĩa biến)


#rut gon if - else

n = int(input("n="))

if n%3 ==0:
    print("n chia het cho 3")
else:
    print("n khong chia het cho 3")

#=>
print("n chia het cho 3" if n%3 == 0 else"N khong chia het cho 3")


a = int(input('a ='))
b = int(input('b ='))

if a > b:
    print(a)
else:
    print(b)

#=>
print(a if a>b else b)

# cach khac 
m=a 
if b>a:
    m=b
print(m)

#Vi du khac
a,b = map(int, input().split())

print(a if a<b else b)


#eval
# danh gia cai bieu thuc nam ben trong cai chuoi
# chi convert ddc so  va so thuc

print(eval("1+2 ** 4"))

print(eval("1"))

print(eval("1.25"))

a,b = map(eval,input().split())

print(a)
print(b)

# nhap nhieu hon thi convert ve list
lts = list(map(eval,input().split()))

print(lts)


# 
lst = [1,2,3,4]
# 1 2 3 4 
print(*lst)
#tuong duong
print(1,2,3,4)
# 1 % 2 % 3 % 4
print(*lst,sep="$")


# lam tron format
x=2.4567
print(format(x,".2f"))

#roud
x=2.456
print(round(x))
print(round(x,2))

#pow(mu~)
print(pow(2,3))
print(pow(2.0,3))

#sorted => new list sap xep
lst = [4,3,2,10]
new_lst = sorted(lst)
print(new_lst)

lst = [4,3,2,10]
#giam dan
new_lst = sorted(lst,reverse=True)
print(new_lst)

#chr - ord 
char = 'a'

print("ASCII code:",ord(char))

char = 'A'

print("ASCII code:",ord(char))

#ord - chr
ascii_code = 97 
print(chr(ascii_code)) #a

#list
s = "abcd"
print(list(s)) #['a','b','c','d']
lst = list(map(eval,input().split()))
print(lst)

#divmod
print(divmod(4,3))

tup = divmod(11,3) #11/3=3 , 11%3 =3
print(tup)

thuong, phan_du= divmod(11,3) #11/3=3 , 11%3 =3
print(thuong)
print(phan_du)


#bin(he 10 thanh he 2)
int_number =10
'''0b1010'''
binary_string = bin(int_number)
print(binary_string[2:])

print(format(int_number,'b'))

print(f"{int_number:b}")








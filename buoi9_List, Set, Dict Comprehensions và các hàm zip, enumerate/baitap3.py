#Cho dict như sau:
import json

people = {
  "Emma": 71,
  "Jack": 45,
  "Amy": 15,
  "Ben": 29
}

# In ra người già nhất
# c1
old = max(people, key=people.get)
print(old,people[old])

print(max(people, key=people.get))

# c2
max_age = max(people.values())
for name,age in people.items():
    if age == max_age:
        print(name,age)
    break

# Tạo ra một dict mới dựa vào people dict với tuổi của mỗi người tăng gấp đôi
new_dict_age = {
    key : value * 2
    for key,value in people.items()
}
print(new_dict_age)
print(json.dumps(new_dict_age, indent=4))

# In ra enumerate các key trong people dict
print(list(enumerate(people)))

# Sử dụng hàm dict để biến enumerate bên trên trở thành dict
print(dict(enumerate(people)))
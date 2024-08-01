# Sử dụng zip function để tạo 2 lists sau trở thành một dict

import json

fruits = ["banana", "apple", "kiwi", "mango", "cherry", "orange"]

amounts = [12, 34, 90, 100, 300, 45, 60, 70, 678]

dict_fr_am = dict(zip(fruits,amounts))
print(dict_fr_am)

print(json.dumps(dict_fr_am, indent=4))
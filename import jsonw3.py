# Chuyển đổi các đối tượng Python thành chuỗi JSON và in các giá trị:

# import json

# print(json.dumps({"name": "John", "age": 30}))
# print(json.dumps(["apple", "bananas"]))
# print(json.dumps(("apple", "bananas")))
# print(json.dumps("hello"))
# print(json.dumps(42))
# print(json.dumps(31.76))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None))


import json
x = {
     "name" : "John",
     "age"  : 30
    }
y = json.dumps(x)
print(y)
from itertools import combinations

# Tập mục đơn
items = ['a', 'c', 'd', 't', 'w']

# Tạo các tập mục đôi, ba, ...
max_length = len(items)

# Tạo tất cả các tập mục có thể từ tập mục đơn đến tập mục có độ dài tùy ý
itemsets = []
for length in range(1, max_length + 1):
    itemsets.extend(combinations(items, length))

# In ra các tập mục
for itemset in itemsets:
    print(itemset)

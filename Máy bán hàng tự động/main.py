class VendingMachine:
    def __init__(self, num_items, item_price):
        # Khởi tạo với số lượng mặt hàng và giá mỗi mặt hàng
        self.num_items = num_items
        self.item_price = item_price

    def buy(self, req_items, money):
        # Kiểm tra có đủ mặt hàng hay không
        if req_items > self.num_items:
            raise ValueError("Không đủ mặt hàng trong máy")
        
        # Kiểm tra số tiền khách đưa vào có đủ không
        total_cost = req_items * self.item_price
        if money < total_cost:
            raise ValueError("Không đủ tiền")
        
        # Nếu giao dịch thành công, giảm số lượng mặt hàng và trả lại tiền thừa
        self.num_items -= req_items
        return money - total_cost  # Trả lại tiền thừa
    
# Ví dụ sử dụng
if __name__ == "__main__":
    vm = VendingMachine(10, 5)  # 10 mặt hàng, mỗi mặt hàng giá 5 đồng
    try:
        change = vm.buy(3, 20)  # Mua 3 mặt hàng với 20 đồng
        print(f"Mua hàng thành công! Tiền thừa: {change}")
    except ValueError as e:
        print(e)

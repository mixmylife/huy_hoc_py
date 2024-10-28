# Tạo menu có các chức năng của một app quản lý sách
# Thêm 1 cuốn sách
# Hiển thị tất cả các cuốn sách
# Xóa các cuốn sách theo id 
# Tìm kiếm các cuốn sách theo id
# Lưu ý: Dữ liệu về các cuốn sách lưu trữ trong file json

import json

USER_MENU = """
Các chức năng:
        'a' : Thêm một cuốn sách
        'd' : Hiển thị tất cả các cuốn sách
        'r' : Xóa các cuốn sách theo id
        'f' : Tìm kiếm sách theo id
        'q' : Thoát

        Nhập lựa chọn của bạn:
"""

book_file = "if_book.json"
prevs = set()

# Khởi tạo tệp JSON nếu chưa có
try:
    with open(book_file, 'x') as file_book:
        json.dump([], file_book)
except FileExistsError:
    pass

def add_book():
    book_id = input("Nhập id cuốn sách: ")
    while book_id in prevs:
        print("ID bị trùng, vui lòng nhập lại.")
        book_id = input("Nhập id cuốn sách: ")

    name = input("Nhập tên cuốn sách: ")
    author = input("Nhập tên tác giả: ")
    release_year = input("Nhập năm xuất bản: ")

    new_book = {
        "id": book_id,
        "name": name,
        "author": author,
        "release_year": release_year,
    }

    # Đọc dữ liệu hiện tại và thêm sách mới
    with open(book_file, 'r+') as file:
        lst_book = json.load(file)
        lst_book.append(new_book)
        file.seek(0)
        json.dump(lst_book, file, indent=4)

    print("Thêm thành công!")
    prevs.add(book_id)

def show_book(book):
    print(f"Name: {book['name']} - Author: {book['author']} - Release Year: {book['release_year']}")

def show_all_book():
    with open(book_file, 'r') as file:
        lst_book = json.load(file)
    if lst_book:
        for idx, book in enumerate(lst_book, start=1):
            print(f"Vị trí: {idx}")
            show_book(book)
    else:
        print("Danh sách trống!")

def find_book():
    with open(book_file, 'r') as file:
        lst_book = json.load(file)
    if lst_book:
        book_id = input("Nhập id cuốn sách muốn tìm: ")
        for book in lst_book:
            if book['id'] == book_id:
                show_book(book)
                return
        print(f"Không tìm thấy sách có id là: {book_id}")
    else:
        print("Danh sách trống!")

def delete_book():
    with open(book_file, 'r') as file:
        lst_book = json.load(file)
    if lst_book:
        book_id = input("Nhập id cuốn sách muốn xóa: ")
        updated_books = [book for book in lst_book if book['id'] != book_id]

        if len(updated_books) == len(lst_book):
            print(f"Không tìm thấy sách có id là: {book_id}")
        else:
            with open(book_file, 'w') as file:
                json.dump(updated_books, file, indent=4)
            print(f"Đã xóa sách có id là: {book_id}")
    else:
        print("Danh sách trống!")

# Lựa chọn menu
choose = {
    'a': add_book,
    'd': show_all_book,
    'r': delete_book,
    'f': find_book,
}

while True:
    user_choice = input(USER_MENU).strip().lower()

    if user_choice in choose:
        choose[user_choice]()
    elif user_choice == 'q':
        print("Đã thoát khỏi chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại.")
    

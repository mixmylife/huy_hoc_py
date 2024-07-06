import turtle
import random

# Thiết lập màn hình
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')

# Tạo đối tượng con rùa
t = turtle.Turtle()
t.speed(0)  # Đặt tốc độ nhanh nhất
t.hideturtle()  # Ẩn con rùa

# Hàm vẽ hình trái tim
def draw_heart(x, y, size):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.color('red', 'red')
    t.left(140)
    t.forward(224 * size)
    for _ in range(200):
        t.right(1)
        t.forward(2 * size)
    t.left(120)
    for _ in range(200):
        t.right(1)
        t.forward(2 * size)
    t.left(140)
    t.forward(224 * size)
    t.end_fill()

# Hàm vẽ chữ
def draw_text(message, x, y, font_size=20):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color('white')
    t.write(message, align='center', font=('Arial', font_size, 'bold'))

# Hàm vẽ pháo hoa
def draw_firework(x, y):
    colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple']
    t.penup()
    t.goto(x, y)
    t.pendown()
    for _ in range(36):
        t.color(random.choice(colors))
        t.forward(50)
        t.backward(50)
        t.right(10)
    t.penup()

# Hàm vẽ sao
def draw_star(x, y, size):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.color('yellow')
    for _ in range(5):
        t.forward(50 * size)
        t.right(144)
    t.end_fill()
    t.penup()

# Hàm vẽ bong bóng
def draw_bubble(x, y, size):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.color('lightblue')
    t.circle(50 * size)
    t.end_fill()
    t.penup()

# Hàm vẽ hoa
def draw_flower(x, y, size):
    colors = ['red', 'blue', 'yellow', 'orange', 'purple', 'pink']
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color('green')
    t.begin_fill()
    for _ in range(6):
        t.forward(100 * size)
        t.right(120)
    t.end_fill()
    for _ in range(6):
        t.color(random.choice(colors))
        t.begin_fill()
        t.circle(15 * size)
        t.end_fill()
        t.right(60)
    t.penup()

# Vẽ hình trái tim
draw_heart(0, 0, 0.5)

# Vẽ các dòng chữ chúc mừng
draw_text("Happy Birthday", 0, 150, font_size=30)
draw_text("to My Love Duyn", 0, 100, font_size=30)

# Tạo hiệu ứng đẹp
for _ in range(10):
    x = random.randint(-400, 400)
    y = random.randint(-200, 200)
    draw_firework(x, y)

for _ in range(5):
    x = random.randint(-300, 300)
    y = random.randint(-200, 200)
    draw_star(x, y, random.uniform(0.5, 1.5))

for _ in range(5):
    x = random.randint(-300, 300)
    y = random.randint(-200, 200)
    draw_bubble(x, y, random.uniform(0.5, 1.5))

for _ in range(3):
    x = random.randint(-300, 300)
    y = random.randint(-200, 200)
    draw_flower(x, y, random.uniform(0.5, 1.5))

# Ẩn con rùa và hiển thị kết quả
t.hideturtle()
screen.mainloop()

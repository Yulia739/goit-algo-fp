import turtle

# Функція для малювання дерева Піфагора
def draw_pythagoras_tree(t, length, angle, level):
    if level == 0:
        return

    # Малюємо поточну гілку
    t.forward(length)

    # Перехід до наступної гілки
    t.left(angle)

    # Рекурсивний виклик для лівої гілки
    draw_pythagoras_tree(t, length * 0.7, angle, level - 1)

    t.right(2 * angle)

    # Рекурсивний виклик для правої гілки
    draw_pythagoras_tree(t, length * 0.7, angle, level - 1)

    t.left(angle)

    # Повертаємось до початкової позиції
    t.backward(length)

# Функція для ініціалізації і налаштування малювання
def setup_tree(level):
    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)  # Швидкість малювання
    t.left(90)  # Початковий кут
    t.penup()
    t.backward(200)  # Початкова позиція
    t.pendown()

    # Початкова довжина, кут і рівень рекурсії
    initial_length = 100
    angle = 30

    # Малюємо дерево Піфагора
    draw_pythagoras_tree(t, initial_length, angle, level)

    # Завершуємо малювання
    turtle.done()

level = int(input("Введіть рівень рекурсії: "))
setup_tree(level)

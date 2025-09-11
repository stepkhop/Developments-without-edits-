from math import *
import math
import matplotlib.pyplot as plt

# Класс для представления 2D вектора:
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Умножение вектора на скаляр (изменение длины)
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    # Сложение двух векторов
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    # Поворот вектора на заданный угол (в радианах)
    def rotate(self, angle):
        cos_a = cos(angle)
        sin_a = sin(angle)
        new_x = self.x * cos_a - self.y * sin_a
        new_y = self.x * sin_a + self.y * cos_a
        return Vector(new_x, new_y)

    # Строковое представление вектора для удобного вывода
    def __str__(self):
        return f"({self.x}, {self.y})"


# Класс для представления узла бинарного дерева ветвей:
class Tree:
    def __init__(self, start_point, end_point):
        self.start_point = start_point  # Начальная точка ветви (Vector)
        self.end_point = end_point  # Конечная точка ветви (Vector)
        self.left = None  # Левое поддерево (Tree или None)
        self.right = None  # Правое поддерево (Tree или None)


# Рекурсивная функция генерации бинарного дерева ветвей:
def generation_Tree(start_point, direction, length, depth, k, angle):
    # Базовый случай рекурсии - достигнута максимальная глубина:
    if depth == 0:
        return None

    # Вычисление конечной точки текущей ветви:
    end_point = start_point + direction * length

    # Создание нового узла дерева:
    tree = Tree(start_point, end_point)

    # Вычисление направлений для ветвей:
    left_dir = direction.rotate(-angle)  # Поворот против часовой стрелки
    right_dir = direction.rotate(angle)  # Поворот по часовой стрелке

    # Рекурсивное построение левого и правого поддеревьев:
    tree.left = generation_Tree(end_point, left_dir, length * k, depth - 1, k, angle)
    tree.right = generation_Tree(end_point, right_dir, length * k, depth - 1, k, angle)

    return tree


# Функция рекурсивного вывода структуры дерева в консоль:
def print_tree(tree, level=0):
    if tree:
        indent = "  " * level  # Формирование отступа для визуализации уровней
        print(f"{indent}Level {level}: {tree.start_point} -> {tree.end_point}")
        # Рекурсивный вывод левого и правого поддеревьев
        print_tree(tree.left, level + 1)
        print_tree(tree.right, level + 1)


# Функция для отрисовки дерева и сохранения в PNG:
def draw_tree(tree, filename):
    fig, ax = plt.subplots(figsize = (10, 8))

    def draw_branch(node):
        if node:
            # Рисуем линию ветви:
            start_x, start_y = node.start_point.x, node.start_point.y
            end_x, end_y = node.end_point.x, node.end_point.y

            ax.plot([start_x, end_x], [start_y, end_y], 'b-', linewidth = 2)

            # Рекурсивно рисуем дочерние ветви:
            draw_branch(node.left)
            draw_branch(node.right)

    draw_branch(tree)
    ax.set_aspect('equal')
    ax.grid(True, alpha = 0.3)
    plt.title(f'Binary Tree - {filename}')
    plt.savefig(filename, dpi = 300, bbox_inches='tight')
    plt.close()


# Функция для создания трех различных тестовых изображений:
def visualize_and_save_tests():
    # Тест 1: Первое дерево
    tree1 = generation_Tree(Vector(0, 0), Vector(0, 1), 100, 3, 0.7, radians(45))
    draw_tree(tree1, "test1_one_tree.png")
    print("\nТест 1 - Первое дерево:")
    print_tree(tree1)

    # Тест 2: Второе дерево
    tree2 = generation_Tree(Vector(0, 0), Vector(0, 1), 80, 4, 0.8, radians(30))
    draw_tree(tree2, "test2_two_tree.png")
    print("\nТест 2 - Второе дерево:")
    print_tree(tree2)

    # Тест 3: Третье дерево
    tree3 = generation_Tree(Vector(-30, 10), Vector(0, 1), 120, 2, 0.6, radians(60))
    draw_tree(tree3, "test3_three_tree.png")
    print("\nТест 3 - Третье дерево:")
    print_tree(tree3)


# Функция для получения данных от пользователя:
def request_for_user():
    # Запрос координат начальной точки
    print("Введите начальную точку X: ")
    start_x = float(input())
    print("Введите начальную точку Y: ")
    start_y = float(input())

    # Запрос параметров генерации дерева
    print("Введите глубину дерева: ")
    depth = int(input())
    print("Введите начальную длину ветви: ")
    length = float(input())
    print("Введите коэффициент уменьшения: ")
    k = float(input())
    print("Введите угол расхождения ветвей (в градусах): ")
    angle_degrees = float(input())

    # Преобразование угла из градусов в радианы:
    angle_radians = math.radians(angle_degrees)

    # Создание начальной точки и начального направления:
    start_point = Vector(start_x, start_y)
    initial_direction = Vector(0, 1)  # Начальное направление - вверх по оси Y

    # Генерация дерева с заданными параметрами:
    tree_generation = generation_Tree(start_point, initial_direction, length, depth, k, angle_radians)

    # Вывод полученной структуры дерева:
    print("\nСтруктура дерева:")
    print_tree(tree_generation)


# Запускаем код:
if __name__ == "__main__":
    # Задача 1: Вывод структуры дерева в консоль
    request_for_user()

    # Задача 2: Создание трех различных изображений PNG
    print("\n" + "=" * 50)
    print("Создание тестовых изображений...")
    visualize_and_save_tests()
    print("\nИзображения сохранены как:")
    print("1. test1_one_tree.png")
    print("2. test2_two_tree.png")
    print("3. test3_three_tree.png")

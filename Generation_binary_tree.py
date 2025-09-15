from math import *
from Visualization_binary_tree import print_tree
from Create_picture import visualize_and_save_tests
from requesting_parameters import request_for_user

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
        self.left = list()
        self.right = list()

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


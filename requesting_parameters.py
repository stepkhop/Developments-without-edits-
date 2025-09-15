from function_for_data_entry import get_input
import math
from Generation_binary_tree import Vector
from Generation_binary_tree import print_tree
from recursion_function_for_binary_tree import generation_Tree

def request_for_user():
    # Запрос всех параметров
    start_x = get_input("Введите начальную точку X: ")
    start_y = get_input("Введите начальную точку Y: ")
    depth = get_input("Введите глубину дерева: ", int)
    length = get_input("Введите начальную длину ветви: ")
    k = get_input("Введите коэффициент уменьшения: ")
    angle_degrees = get_input("Введите угол расхождения ветвей (в градусах): ")

    # Преобразование и создание объектов
    angle_radians = math.radians(angle_degrees)
    start_point = Vector(start_x, start_y)
    initial_direction = Vector(0, 1)

    # Генерация дерева
    tree_generation = generation_Tree(
        start_point, initial_direction, length, depth, k, angle_radians
    )

    print("\nСтруктура дерева:")
    print_tree(tree_generation)

    return tree_generation
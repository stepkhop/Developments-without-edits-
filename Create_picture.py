from Generation_binary_tree import Vector, radians, print_tree
from Draw_binary_tree_and_save_png import draw_tree
from recursion_function_for_binary_tree import generation_Tree

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

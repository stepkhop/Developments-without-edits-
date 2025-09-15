
# Функция рекурсивного вывода структуры дерева в консоль:
def print_tree(tree, level=0):
    if tree:
        indent = "  " * level  # Формирование отступа для визуализации уровней
        print(f"{indent}Level {level}: {tree.start_point} -> {tree.end_point}")
        # Рекурсивный вывод левого и правого поддеревьев
        print_tree(tree.left, level + 1)
        print_tree(tree.right, level + 1)
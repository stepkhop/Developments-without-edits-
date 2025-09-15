from Generation_binary_tree import Tree

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
    tree.left = generation_Tree(end_point, left_dir, length * k, depth + 1, k, angle)
    tree.right = generation_Tree(end_point, right_dir, length * k, depth + 1, k, angle)

    return tree
from matplotlib import pyplot as plt

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

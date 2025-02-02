import uuid
import networkx as nx
import matplotlib.pyplot as plt
import random


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        """ Вставка нового елемента в дерево """
        new_node = Node(key)
        if not self.root:
            self.root = new_node
        else:
            self._insert(self.root, new_node)

    def _insert(self, current, new_node):
        """ Рекурсивна вставка нового елемента в дерево """
        if new_node.val < current.val:
            if current.left is None:
                current.left = new_node
            else:
                self._insert(current.left, new_node)
        else:
            if current.right is None:
                current.right = new_node
            else:
                self._insert(current.right, new_node)

    def visualize_tree(self):
        """ Візуалізація дерева """
        tree = nx.DiGraph()
        pos = {self.root.id: (0, 0)}
        tree = self._add_edges(tree, self.root, pos)

        colors = [node[1]['color'] for node in tree.nodes(data=True)]
        labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

        plt.figure(figsize=(8, 5))
        nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
        plt.show()

    def _add_edges(self, graph, node, pos, x=0, y=0, layer=1):
        """ Додавання ребер в граф для візуалізації дерева """
        if node is not None:
            graph.add_node(node.id, color=node.color, label=node.val)
            if node.left:
                graph.add_edge(node.id, node.left.id)
                l = x - 1 / 2 ** layer
                pos[node.left.id] = (l, y - 1)
                l = self._add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
            if node.right:
                graph.add_edge(node.id, node.right.id)
                r = x + 1 / 2 ** layer
                pos[node.right.id] = (r, y - 1)
                r = self._add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
        return graph

    def dfs(self):
        """ Обхід в глибину (DFS) з ітерацією за допомогою стеку """
        stack = [self.root]
        visited = set()
        order = 0

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                # Генерація унікального кольору на основі порядку обходу
                color = "#{:02X}{:02X}{:02X}".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                node.color = color
                node.val = f"{node.val} ({order})"
                order += 1
                # Додаємо праву і ліву дочірні вершини, якщо вони є
                if node.right and node.right not in visited:
                    stack.append(node.right)
                if node.left and node.left not in visited:
                    stack.append(node.left)
        self.visualize_tree()

    def bfs(self):
        """ Обхід в ширину (BFS) з ітерацією за допомогою черги """
        queue = [self.root]
        visited = set()
        order = 0

        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                # Генерація унікального кольору на основі порядку обходу
                color = "#{:02X}{:02X}{:02X}".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                node.color = color
                node.val = f"{node.val} ({order})"
                order += 1
                # Додаємо ліву і праву дочірні вершини в чергу
                if node.left and node.left not in visited:
                    queue.append(node.left)
                if node.right and node.right not in visited:
                    queue.append(node.right)
        self.visualize_tree()


# Тестування

# Створення дерева
tree = BinaryTree()
tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(2)
tree.insert(7)
tree.insert(12)
tree.insert(18)

# Візуалізація обходу в глибину
print("Обхід в глибину (DFS):")
tree.dfs()

# Візуалізація обходу в ширину
print("Обхід в ширину (BFS):")
tree.bfs()

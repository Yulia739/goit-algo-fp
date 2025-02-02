import uuid
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла


class BinaryHeap:
    def __init__(self):
        self.heap = []

    def insert(self, key):
        """ Вставка нового елемента в мін-купу """
        new_node = Node(key)
        self.heap.append(new_node)
        if len(self.heap) == 1:
            self.root = new_node
        else:
            self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        """ Переміщення елемента вгору до задоволення властивості мін-купи """
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index].val < self.heap[parent_index].val:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._heapify_up(parent_index)

    def build_heap(self, values):
        """ Створення купи з масиву значень """
        self.heap = [Node(val) for val in values]
        for i in range(len(self.heap) // 2, -1, -1):
            self._heapify_down(i)

        # Побудова зв'язків між батьками та нащадками
        for i in range(len(self.heap)):
            left_index = 2 * i + 1
            right_index = 2 * i + 2
            if left_index < len(self.heap):
                self.heap[i].left = self.heap[left_index]
            if right_index < len(self.heap):
                self.heap[i].right = self.heap[right_index]

        self.root = self.heap[0]

    def _heapify_down(self, index):
        """ Переміщення елемента вниз до задоволення властивості мін-купи """
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2
        if left < len(self.heap) and self.heap[left].val < self.heap[smallest].val:
            smallest = left
        if right < len(self.heap) and self.heap[right].val < self.heap[smallest].val:
            smallest = right
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

    def visualize_heap(self):
        """ Візуалізація бінарної купи """
        tree = nx.DiGraph()
        pos = {self.root.id: (0, 0)}
        tree = self._add_edges(tree, self.root, pos)

        colors = [node[1]['color'] for node in tree.nodes(data=True)]
        labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

        plt.figure(figsize=(8, 5))
        nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
        plt.show()

    def _add_edges(self, graph, node, pos, x=0, y=0, layer=1):
        """ Додавання ребер в граф для візуалізації купи """
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


# Тестування
heap = BinaryHeap()

# Вставка елементів у мін-купу
values = [10, 20, 5, 6, 1, 8, 9]
heap.build_heap(values)

# Візуалізація мін-купи
heap.visualize_heap()

import heapq

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = {i: [] for i in range(vertices)}  # Словник для зберігання графа

    # Додаємо ребро до графа
    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))  # Оскільки граф ненапрямлений

    # Алгоритм Дейкстри з використанням бінарної купи
    def dijkstra(self, start):
        # Відстань до всіх вершин від початкової (нескінченність)
        distances = {i: float('inf') for i in range(self.vertices)}
        distances[start] = 0  # Відстань від початкової до себе рівна нулю

        # Купа (мін-купа) для вибору вершини з мінімальною відстанню
        min_heap = [(0, start)]  # (відстань, вершина)
        
        while min_heap:
            # Вибираємо вершину з мінімальною відстанню
            current_distance, current_vertex = heapq.heappop(min_heap)
            
            # Якщо поточна відстань більша, ніж відома мінімальна, пропускаємо її
            if current_distance > distances[current_vertex]:
                continue

            # Перевіряємо сусідів поточної вершини
            for neighbor, weight in self.graph[current_vertex]:
                distance = current_distance + weight
                
                # Якщо знайдено коротший шлях до сусіда, оновлюємо його
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(min_heap, (distance, neighbor))  # Додаємо нову пару в купу

        return distances

# Тестування
graph = Graph(6)  # Створюємо граф з 6 вершинами

# Додаємо ребра (u, v, weight)
graph.add_edge(0, 1, 7)
graph.add_edge(0, 2, 9)
graph.add_edge(0, 5, 14)
graph.add_edge(1, 2, 10)
graph.add_edge(1, 3, 15)
graph.add_edge(2, 3, 11)
graph.add_edge(2, 5, 2)
graph.add_edge(3, 4, 6)
graph.add_edge(4, 5, 9)

# Застосовуємо алгоритм Дейкстри
distances = graph.dijkstra(0)  # Початкова вершина 0

# Виводимо найкоротші шляхи від вершини 0 до всіх інших
print("Відстані від вершини 0 до інших вершин:")
for vertex in range(6):
    print(f"До вершини {vertex}: {distances[vertex]}")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Додаємо новий елемент у кінець списку
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # Функція для реверсування списку
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # Функція для виведення списку
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


    # Функція для сортування вставками
    def insertion_sort(self):
        if not self.head or not self.head.next:
            return
        sorted_list = None
        current = self.head
        while current:
            next_node = current.next
            if not sorted_list or sorted_list.data >= current.data:
                current.next = sorted_list
                sorted_list = current
            else:
                temp = sorted_list
                while temp.next and temp.next.data < current.data:
                    temp = temp.next
                current.next = temp.next
                temp.next = current
            current = next_node
        self.head = sorted_list


    # Функція для об'єднання двох відсортованих списків
    def merge_sorted_lists(self, other_list):
        p1 = self.head
        p2 = other_list.head
        merged_list = LinkedList()

        while p1 and p2:
            if p1.data <= p2.data:
                merged_list.append(p1.data)
                p1 = p1.next
            else:
                merged_list.append(p2.data)
                p2 = p2.next

        while p1:
            merged_list.append(p1.data)
            p1 = p1.next

        while p2:
            merged_list.append(p2.data)
            p2 = p2.next

        return merged_list   


# Тестування реверсування
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)

print("Оригінальний список:")
ll.print_list()

ll.reverse()

print("Реверсований список:")
ll.print_list()


# Тестування сортування вставками
ll = LinkedList()
ll.append(4)
ll.append(1)
ll.append(3)
ll.append(2)

print("Невідсортований список:")
ll.print_list()

ll.insertion_sort()

print("Відсортований список:")
ll.print_list()


# Тестування об'єднання двох списків
ll1 = LinkedList()
ll1.append(1)
ll1.append(3)
ll1.append(5)

ll2 = LinkedList()
ll2.append(2)
ll2.append(4)
ll2.append(6)

print("Перший список:")
ll1.print_list()

print("Другий список:")
ll2.print_list()

merged = ll1.merge_sorted_lists(ll2)

print("Об'єднаний список:")
merged.print_list()
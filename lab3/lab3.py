from collections import deque


print("Ляшенко Илья Денисович")
print("РПИа-о23")
#Реализация стека через массив


class StackArray:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

#Через связанный список
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
#С использованием стандартной библиотеки
class StackLinkedList:
    def __init__(self):
        self.head = None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if not self.is_empty():
            item = self.head.data
            self.head = self.head.next
            return item
        return None

    def is_empty(self):
        return self.head is None

    def peek(self):
        if not self.is_empty():
            return self.head.data
        return None


#С использованием стандартной библиотеки



class StackDeque:
    def __init__(self):
        self.stack = deque()

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None
        
#Реализация очереди через массив

class QueueArray:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    def is_empty(self):
        return len(self.queue) == 0
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
#Через связанный список
class QueueLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, item):
        new_node = Node(item)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None
        return temp.data

    def is_empty(self):
        return self.front is None
#С использованием стандартной библиотеки:

class QueueDeque:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        return None

    def is_empty(self):
        return len(self.queue) == 0


def dfs(maze, start, end):
    
    stack = [(start, [start])]
    visited = set()

    while stack:
        (current, path) = stack.pop()
        if current in visited:
            continue
        visited.add(current)

        x, y = current
        if current == end:
            return path
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == 0:
                stack.append(((nx, ny), path + [(nx, ny)]))
    
    return None

def bfs(maze, start, end):
    
    queue = [(start, [start])]
    visited = set([start])

    while queue:
        (current, path) = queue.pop(0)
        x, y = current
        
        if current == end:
            return path
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == 0 and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), path + [(nx, ny)]))
    
    return None  # Путь не найден


# Пример использования:
maze = [
    [0, 1, 1, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 0]
]
start = (0, 0)
end = (3, 3)

# Проверка DFS
path = dfs(maze, start, end)
if path is None:
    print("DFS: Путь не найден")
else:
    print(f"DFS Path: {path}")

# Проверка BFS
path = bfs(maze, start, end)
if path is None:
    print("BFS: Путь не найден")
else:
    print(f"BFS Path: {path}")

